#include <main.h>

struct mp3_state_struct {
   int state;
   int dig1;
   int dig2;
   int dig3;
   int dig4;
};

int seven, chiff, mask, i;
struct mp3_state_struct st1, st2, last_state;

// Optimisation de la lecture de l'état actuel de l'afficheur
// 120µs/appel
void mp3_inst_state() {
   output_low(CLK_PIN);
   
   // Parallel Register Load
   output_high(PS_PIN);
   
   output_high(CLK_PIN);
   output_low(CLK_PIN);
   
   // Serial Shift Register
   output_low(PS_PIN);
   
   chiff = 0;
   seven = 0;
   
   // G, F, E
   if (input(DO21_PIN)) bit_set(seven, 6);
   if (input(DO22_PIN)) bit_set(seven, 5);
   if (input(DO23_PIN)) bit_set(seven, 4);
   
   // C5, C4, C3
   if (input(DO11_PIN)) bit_set(chiff, 4);
   if (input(DO12_PIN)) bit_set(chiff, 3);
   if (input(DO13_PIN)) bit_set(chiff, 2);
      
   output_high(CLK_PIN);
   output_low(CLK_PIN);
   
   output_high(CLK_PIN);
   output_low(CLK_PIN);
   
   output_high(CLK_PIN);
   output_low(CLK_PIN);
   
   // D, C, B
   if (input(DO21_PIN)) bit_set(seven, 3);
   if (input(DO22_PIN)) bit_set(seven, 2);
   if (input(DO23_PIN)) bit_set(seven, 1);
   
   // C2, C1
   if (input(DO11_PIN)) bit_set(chiff, 1);
   if (input(DO12_PIN)) bit_set(chiff, 0);
     
   output_high(CLK_PIN);
   output_low(CLK_PIN);
  
   // A
   if (input(DO23_PIN)) bit_set(seven, 0);   
}

char mp3_get_digit(int sev) {
   if (sev == 0x40) return '0';
   if (sev == 0x79) return '1';
   if (sev == 0x24) return '2';
   if (sev == 0x30) return '3';
   if (sev == 0x19) return '4';
   if (sev == 0x12) return '5';
   if (sev == 0x02) return '6';
   if (sev == 0x78) return '7';
   if (sev == 0x00) return '8';
   if (sev == 0x10) return '9';
   if (sev == 0x7F) return ' ';
   if (sev == 0x0C) return 'P';
   if (sev == 0x08) return 'A';
   if (sev == 0x06) return 'E';
   if (sev == 0x41) return 'U';
   if (sev == 0x2F) return 'R';
   if (sev == 0x48) return 'N';
   if (sev == 0x0E) return 'F';
   if (sev == 0x47) return 'L';
   return sev;
}

int cmp_state_eq(struct mp3_state_struct state, struct mp3_state_struct last_state) {
   if (state.state != last_state.state) return FALSE;
   if (state.dig1 != last_state.dig1) return FALSE;
   if (state.dig2 != last_state.dig2) return FALSE;
   if (state.dig3 != last_state.dig3) return FALSE;
   if (state.dig4 != last_state.dig4) return FALSE;
   return TRUE;
}


// Lecture de l'état des 5 chiffres de l'afficheur
int mp3_state() {
   for (i = 0 ; i < 3 ; i++) {
       do {
         mp3_inst_state();
      } while (chiff != 0x02);
      st1.dig3 = seven;
      
      do {
         mp3_inst_state();
      } while (chiff != 0x01);
      st1.dig4 = seven;
      
      do {
         mp3_inst_state();
      } while (chiff != 0x10);
      st1.state = seven;
      
      do {
         mp3_inst_state();
      } while (chiff != 0x08);
      st1.dig1 = seven;
      
      do {
         mp3_inst_state();
      } while (chiff != 0x04);
      st1.dig2 = seven;     
      
      if (i == 0) {
         memcpy(&st2, &st1, sizeof(st1));
      } else {
         if (cmp_state_eq(st1, st2)) break;
         memcpy(&st2, &st1, sizeof(st1));
         i = 0;
      }
   }
   
   st1.dig1 = mp3_get_digit(st1.dig1);
   st1.dig2 = mp3_get_digit(st1.dig2);
   st1.dig3 = mp3_get_digit(st1.dig3);
   st1.dig4 = mp3_get_digit(st1.dig4);
   
   return TRUE;
}

void main()
{     
   memset(&st1, 0, sizeof(st1));
   memset(&last_state, 0, sizeof(st1));
   
   while (TRUE) {
      if (mp3_state()) {
         putc('!');
         putc(st1.state);
         putc(st1.dig4);
         putc(st1.dig3);
         putc(st1.dig2);
         putc(st1.dig1);
      }
   }
}


#include <infrared.h>

int32 val, mask;
int16 data;
int cpt;
char tche;

int gettouche(int16 data) {
   int *p;
   p = &data;

   switch(p[0]) {
      case 0x94: return 'A';
      case 0x90: return 'B';
      case 0x8C: return 'C';
      case 0x88: return 'D';
      case 0x84: return 'E';
      
      case 0xB8: return '1';
      case 0xB4: return '2';
      case 0xB0: return '3';
      case 0xAC: return '4';
      case 0xA8: return '5';
      case 0xA4: return '6';
      case 0xA0: return '7';
      case 0x9C: return '8';
      case 0x98: return '9';
      case 0xD4: return 'F';
      case 0xBC: return '0';
      case 0xD0: return 'G';
      case 0xFC: return 'H';
      case 0xF4: return 'I';
      case 0xF0: return 'J';
      case 0xF8: return 'K';
      case 0x80: return 'L';
      case 0xCC: return 'M';
      case 0xC8: return 'N';
      case 0xC4: return 'O';
      case 0xC0: return 'P';
      case 0xEC: return 'Q';
      case 0xE8: return 'R';
      case 0xE4: return 'S';
      case 0xE0: return 'T';
   }
   
   return 0xFF;
}

void getirdata() {
   int i, j;
   
   // Attend le départ du signal
   while (input(IR_SIGNAL));
   
   val = 0;
   mask = 1;
   j = 0;
   do {
      set_timer0(0);
      while (!input(IR_SIGNAL)) ;
      cpt = get_timer0();
      set_timer0(0);
      mask = mask << 1;
      if (cpt > 0x4f) {
         mask = mask << 1;
      }
      
      while (input(IR_SIGNAL) && get_timer0() < 200) ;
      cpt = get_timer0();
      set_timer0(0);
      if (cpt == 200) break;
      val = val | mask;
      mask = mask << 1;
      if (cpt > 0x4f) {
         val = val | mask;
         mask = mask << 1;
      }
   } while (cpt != 200);
   
   // analyse des données
   data = 0;
   val = val >> 1;
   for (i = 1 ; mask > 0 ; i+=2) {
      data = (data << 1);
      if (!bit_test(val, 0) && bit_test(val, 1)) data |= 1;
      mask = mask >> 2;
      val = val >> 2;
   }
}

#INT_EXT
void ext_isr() {
   output_low(IR_DATA_READY);
   putc(tche);
}

void main()
{
   setup_timer_0(RTCC_INTERNAL | RTCC_DIV_16);
   
   ext_int_edge(0, H_TO_L);
   enable_interrupts(INT_EXT);
   enable_interrupts(GLOBAL);
   
   while (1) {
      getirdata();
      tche = gettouche(data);
      if (tche != 0xff) {
         output_high(IR_DATA_READY);
      }
   }
}

#include <afficheurs.h>

// BESMELLEH ARRAHMEN ARRAHIM
// 12345678901234567890123456
int sz, pa, rm, pos;
int data[32];

int point;
int blink;
int sens;
int chiff_cour;
int16 btm;

int convertToSeg(int v) {
   switch (v) {
      case ' ': return CHIFFRE_ESPACE;
      case '-': return CHIFFRE_TIRET;
      
      case '0': return CHIFFRE_0;
      case '1': return CHIFFRE_1;
      case '2': return CHIFFRE_2;
      case '3': return CHIFFRE_3;
      case '4': return CHIFFRE_4;
      case '5': return CHIFFRE_5;
      case '6': return CHIFFRE_6;
      case '7': return CHIFFRE_7;
      case '8': return CHIFFRE_8;
      case '9': return CHIFFRE_9;
      
      case 'A': 
      case 'a':  return CHIFFRE_A;
      case 'B': 
      case 'b':  return CHIFFRE_B;
      case 'C': 
      case 'c':  return CHIFFRE_C;
      case 'D': 
      case 'd':  return CHIFFRE_D;
      case 'E': 
      case 'e':  return CHIFFRE_E;
      case 'F': 
      case 'f':  return CHIFFRE_F;
      case 'G': 
      case 'g':  return CHIFFRE_G;
      case 'H': 
      case 'h':  return CHIFFRE_H;
      
      case 'I': 
      case 'i':  return CHIFFRE_I;
      case 'J': 
      case 'j':  return CHIFFRE_J;
      case 'K': 
      case 'k':  return CHIFFRE_K;
      case 'L': 
      case 'l':  return CHIFFRE_L;
      case 'M': 
      case 'm':  return CHIFFRE_M;
      case 'N': 
      case 'n':  return CHIFFRE_N;
      case 'O': 
      case 'o':  return CHIFFRE_O;
      case 'P': 
      case 'p':  return CHIFFRE_P;
      
      case 'Q': 
      case 'q':  return CHIFFRE_Q;
      case 'R': 
      case 'r':  return CHIFFRE_R;
      case 'S': 
      case 's':  return CHIFFRE_S;
      case 'T': 
      case 't':  return CHIFFRE_T;
      case 'U': 
      case 'u':  return CHIFFRE_U;
      case 'V': 
      case 'v':  return CHIFFRE_V;
      case 'W': 
      case 'w':  return CHIFFRE_W;
      case 'X': 
      case 'x':  return CHIFFRE_X;
      
      case 'Y': 
      case 'y':  return CHIFFRE_Y;
      case 'Z': 
      case 'z':  return CHIFFRE_Z;
      
      default  : return CHIFFRE_OFF;
   }
}

#INT_RDA
void rda_isr() {
   int c;
   
   c = getch();
   if (c == '!') {
      sz = 0;
      pa = 0;
      rm = TRUE;
      
      data[0] = CHIFFRE_OFF;
      data[1] = CHIFFRE_OFF;
      data[2] = CHIFFRE_OFF;
      data[3] = CHIFFRE_OFF;
   } else if (c == '$') {
      rm = FALSE;
   } else if (c == '*') { // Blinking ON
      blink = TRUE;
      sens = TRUE;
      point = 0x0E;
   } else if (c == '#') { // Blinking OFF
      blink = FALSE;
      point = 0x0F;
   } else if (c < 16) {
      point = c;
   } else {
      if (rm) {
         data[sz] = convertToSeg(c);
         sz++;
         if (sz == 32) {
            rm = FALSE;
         }
      }
   }
   
   clear_interrupt(INT_RDA);
}

#INT_TIMER0 
void timer0_isr() {
   signed int i; 
   int v;
   int1 pt;
  
   output_low(STB_PIN);
   output_low(DATA_PIN);
   output_low(CLK_PIN);
   
   output_low(DIG_EN);
   
   output_bit(DIG_0, bit_test(chiff_cour, 0));
   output_bit(DIG_1, bit_test(chiff_cour, 1));
   output_bit(DIG_2, bit_test(chiff_cour, 2)); 
   
   pos = pa + chiff_cour;
   if (pos >= sz) {
      if (sz > 3) {
         pos = pa + chiff_cour - sz;
         v = data[pos];
      } else {
         v = CHIFFRE_OFF;
      }
   } else {
      v = data[pos];
   }
   pt = bit_test(point, chiff_cour);
   
   for (i = 7 ; i >= 0 ; i--) {
      if (i == 7)
         output_bit(DATA_PIN, pt);
      else
         output_bit(DATA_PIN, bit_test(v, i));
      
      output_high(CLK_PIN);
      output_low(CLK_PIN);
   }
   
   output_high(STB_PIN);
   output_high(DIG_EN);
      
   chiff_cour++;
   if (chiff_cour >= CHIFF_COUNT) { 
      chiff_cour = 0;
   }
   
   btm--;
   if (btm == 0) {
      if (sz > 4) {
         pa++;
         if (pa == sz) pa = 0;
      }
      btm = BLTM;
   }
}

#INT_TIMER1
void timer1_isr() {
   if (!blink) return;
   if (sens) {
      if (point == 0x0e) point = 0x1d;
      else if (point == 0x1d) point = 0x3b;
      else if (point == 0x3b) point = 0x77;
      else if (point == 0x77) {
         sens = FALSE;
      }
   } else {
      if (point == 0x77) point = 0x3b;
      else if (point == 0x3b) point = 0x1d;
      else if (point == 0x1d) point = 0x0e;
      else if (point == 0x0e) {
         sens = TRUE;
      }
   }
}

void main()
{   
   setup_timer_0(RTCC_INTERNAL | RTCC_DIV_8);
   setup_timer_1(T1_INTERNAL | T1_DIV_BY_4);
  
   enable_interrupts(INT_RDA);
   enable_interrupts(INT_TIMER0);
   enable_interrupts(INT_TIMER1);
   enable_interrupts(GLOBAL);
   
   chiff_cour = 0;
   sz = 10;
   pa = 0;
      
   data[0] = convertToSeg('B');
   data[1] = convertToSeg('E');
   data[2] = convertToSeg('S');
   data[3] = convertToSeg('M');
   data[4] = convertToSeg('E');
   data[5] = convertToSeg('L');
   data[6] = convertToSeg('L');
   data[7] = convertToSeg('E');
   data[8] = convertToSeg('H');
   data[9] = convertToSeg(' ');
   
   point = 0x0E;
   blink = TRUE;
   btm = BLTM;
   sens = TRUE;
   
   while (TRUE) {
      
   }
}




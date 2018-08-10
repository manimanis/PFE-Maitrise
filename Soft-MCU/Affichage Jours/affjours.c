#include <affjours.h>

int c;

void show_val(int c) {
   output_bit(PIN_A2, !bit_test(c, 0));
   output_bit(PIN_A7, !bit_test(c, 1));
   output_bit(PIN_A6, !bit_test(c, 2));
   output_bit(PIN_B7, !bit_test(c, 3));
   output_bit(PIN_B6, !bit_test(c, 4));
   output_bit(PIN_B5, !bit_test(c, 5));
   output_bit(PIN_B4, !bit_test(c, 6));
}

#INT_RDA
void  RDA_isr(void) 
{
   c = getch();
   show_val(c);   
}

void main()
{
   for (c = 1 ; c < 128 ; c = c << 1) {
      show_val(c);
      delay_ms(100);
   }
    
   for (c = 128 ; c > 0 ; c = c >> 1) {
      show_val(c);
      delay_ms(100);
   }
    
   delay_ms(1300);
   
   show_val(0);
   
   enable_interrupts(INT_RDA);
   enable_interrupts(GLOBAL);
   
   while (1) {}
}

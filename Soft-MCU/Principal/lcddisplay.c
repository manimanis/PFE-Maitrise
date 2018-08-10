#include "lcddisplay.h"

void lcd_show(char* buffer, int size) {
   int i;
   
   DISABLE_INT;
   for (i = 0 ; i < size ; i++) {
      fputc(buffer[i], lcd);
      delay_ms(20);
   }
   ENABLE_INT;
}

void lcd_putc(char c) {
   DISABLE_INT;
   fputc(c, lcd);
   delay_us(500);
   ENABLE_INT;
}

void lcd_clear() {
   DISABLE_INT;
   fputc(0x1b, lcd);
   delay_us(500);
   fputc('C', lcd);
   delay_us(500);
   ENABLE_INT;
}

void lcd_line_clear() {
   DISABLE_INT;
   fputc(0x1b, lcd);
   delay_us(500);
   fputc('E', lcd);
   delay_us(500);
   ENABLE_INT;
}

void lcd_light(int ison) {
   DISABLE_INT;
   fputc(0x1b, lcd);
   delay_us(500);
   fputc((ison) ? 'N' : 'F', lcd);
   delay_us(500);
   ENABLE_INT;
}

void lcd_gotoxy(int x, int y) {
   DISABLE_INT;
   fputc(0x1b, lcd);
   delay_us(500);
   fputc('G', lcd);
   delay_us(500);
   fputc(x + 0x30, lcd);
   delay_us(500);
   fputc(y + 0x30, lcd);
   delay_us(500);
   ENABLE_INT;
}

void lcd_cur_left() {
   DISABLE_INT;
   fputc(0x1b, lcd);
   delay_us(500);
   fputc('P', lcd);
   delay_us(500);
   fputc('L', lcd);
   delay_us(500);
   ENABLE_INT;
}

void lcd_cur_right() {
   DISABLE_INT;
   fputc(0x1b, lcd);
   delay_us(500);
   fputc('P', lcd);
   delay_us(500);
   fputc('R', lcd);
   delay_us(500);
   ENABLE_INT;
}

void lcd_cur_up() {
   DISABLE_INT;
   fputc(0x1b, lcd);
   delay_us(500);
   fputc('P', lcd);
   delay_us(500);
   fputc('U', lcd);
   delay_us(500);
   ENABLE_INT;
}

void lcd_cur_down() {
   DISABLE_INT;
   fputc(0x1b, lcd);
   delay_us(500);
   fputc('P', lcd);
   delay_us(500);
   fputc('D', lcd);
   delay_us(500);
   ENABLE_INT;
}

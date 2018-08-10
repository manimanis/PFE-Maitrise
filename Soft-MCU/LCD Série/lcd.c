#include <lcd.h>

char c;

char cmd[4];
int is_cmd;
int counter;

char line[32];
int  linepos;
int  refresh;

void serialize_data(int octet) {
   int i, v;
   v = 0x80;
   for (i = 0 ; i < 8 ; i++) {
      if (octet & v) {
         output_high(SH_DATA);
      } else {
         output_low(SH_DATA);
      }
      output_high(SH_CLK);
      output_low(SH_CLK);
      v = v >> 1;
   }
   output_high(SH_STB);
   output_low(SH_STB);
}

void write_lcd_data(int data) {
   output_low(LCD_E);
   
   output_high(LCD_RS);
   
   serialize_data(data);
   
   output_high(LCD_E);
   output_low(LCD_E);
}

void write_lcd_cmd(int data) {
   output_low(LCD_E);
   
   output_low(LCD_RS);
   
   serialize_data(data);
   
   output_high(LCD_E);
   output_low(LCD_E);
}

void initialize_lcd() {
   delay_ms(50);
   
   write_lcd_cmd(0x3C);
   delay_us(50);
   
   write_lcd_cmd(0x0F);
   delay_us(50);
   
   write_lcd_cmd(0x01);
   delay_ms(2);
}

void lcd_clear() {
   write_lcd_cmd(0x01);
   delay_us(50);
}

void lcd_gotoxy(int x, int y) {
   int v;
   v = 0x80 + x;
   if (y) v += 0x40;
   write_lcd_cmd(v);
   delay_us(50);
}

void lcd_gotoposition(int pos) {
   lcd_gotoxy(pos & 0x0f, pos >> 4);
}

void lcd_display_buffer() {
   int i;
   
   DISABLE_INT;
   
   write_lcd_cmd(0x80);
   delay_us(50);
   
   for (i = 0 ; i < 16 ; i++) {
      write_lcd_data(line[i]);
   }
   
   write_lcd_cmd(0xC0);
   delay_us(50);
   
   for (i = 16 ; i < 32 ; i++) {
      write_lcd_data(line[i]);
   }
   
   lcd_gotoposition(linepos);
   
   ENABLE_INT;
}

void lcd_scroll() {
   memcpy(line, line + 16, 16);
   memset(line + 16, 32, 16);
   linepos = 16;
   refresh = TRUE;
}

#int_rda
void isr_rda() {
   c = getch();
   if (c == 0x1b) {
      is_cmd = TRUE;
      counter = 0;
      return ;
   }
   
   if (is_cmd) {
      cmd[counter] = c;
      counter++;
      if (counter >= 4) is_cmd = FALSE;
   } else {
      if (c == 0x0d) {
         if (linepos >= 16) lcd_scroll();
         while (linepos < 16) {
            line[linepos] = ' ';
            linepos++;
         }
         refresh = TRUE;
      } else if (c == 0x08) {
         if (linepos > 0) {
            linepos--;
            line[linepos] = ' ';
            refresh = TRUE;
         }
      } else {
         line[linepos] = c;
         linepos++;
         if (linepos >= 32) {
            lcd_scroll();
         }
         refresh = TRUE;
      }
   }
   clear_interrupt(INT_RDA);
}

void main()
{
   output_low(SH_DATA);
   output_low(SH_CLK);
   output_low(SH_STB);
   
   output_low(LCD_RW);
   output_low(LCD_RS);
   output_low(LCD_E);
   
   output_high(LCD_BKL);
   
   initialize_lcd();
   
   is_cmd = FALSE;
   linepos = 0;
   refresh = FALSE;
   
   memset(line, 32, 32);
   
   delay_ms(2000);
   
   enable_interrupts(INT_RDA);
   enable_interrupts(GLOBAL);
   
   is_cmd = TRUE;
   cmd[0] = 'c';
   counter = 1;
   
   while (TRUE) {
      if (is_cmd) {
         if (counter > 0) {
            // Effacer l'écran
            if (cmd[0] == 'c' || cmd[0] == 'C') {
               lcd_clear();
               memset(line, 32, 32);
               linepos = 0;
               refresh = FALSE;
               is_cmd = FALSE;
            } else 
            // Effacer la ligne en cours
            if (cmd[0] == 'l' || cmd[0] == 'L') {
               if (linepos < 16) {
                  linepos = 0;
                  memset(line, 32, 16);
               } else {
                  linepos = 16;
                  memset(line + 16, 32, 16);
               }
               lcd_gotoposition(linepos);
               is_cmd = FALSE;
               refresh = TRUE;
            } else
            // Supprimer un caractère à droite sans modifier la position du curseur
            if (cmd[0] == 'd' || cmd[0] == 'D') {
               memcpy(line + linepos, line + linepos + 1, 32 - linepos);
               is_cmd = FALSE;
               refresh = TRUE;
               lcd_gotoposition(linepos);
            } else
            // Effacer jusqu'à la fin de la ligne
            if (cmd[0] == 'e' || cmd[0] == 'E') {
               if (linepos < 16) {
                  memset(line + linepos, 32, 16 - linepos);
                  is_cmd = FALSE;
                  refresh = TRUE;
               } else {
                  memset(line + linepos, 32, 32 - linepos);
                  is_cmd = FALSE;
                  refresh = TRUE;
               }
               lcd_gotoposition(linepos);
            } else
            // Activer le rétro-éclairage
            if (cmd[0] == 'n' || cmd[0] == 'N') {
               output_low(LCD_BKL);
            } else
            // désactiver le rétro-éclairage
            if (cmd[0] == 'f' || cmd[0] == 'F') {
               output_high(LCD_BKL);
            } else
            // se positionner
            if ((cmd[0] == 'g' || cmd[0] == 'G') && counter == 3) {
               linepos = (cmd[1] - 0x30) + (cmd[2] - 0x30) << 4;
               lcd_gotoxy(cmd[1] - 0x30, cmd[2] - 0x30);
               is_cmd = FALSE;
               refresh = FALSE;
            } else
            // Mouvement à droite/à gauche/en bas/en haut
            if ((cmd[0] == 'p' || cmd[0] == 'P') && counter == 2) {
               if ((linepos > 0) && (cmd[1] == 'l' || cmd[1] == 'L')) linepos--;
               else if ((linepos < 32) && (cmd[1] == 'r' || cmd[1] == 'R')) linepos++;
               else if ((linepos >= 16) && (cmd[1] == 'u' || cmd[1] == 'U')) linepos -= 16;
               else if ((linepos < 16) && (cmd[1] == 'd' || cmd[1] == 'D')) linepos += 16;
                  
               lcd_gotoposition(linepos);
               is_cmd = FALSE;
               refresh = FALSE;
            }
         }
      }
      if (refresh) {
         refresh = FALSE;
         lcd_display_buffer();
      }
   }
}

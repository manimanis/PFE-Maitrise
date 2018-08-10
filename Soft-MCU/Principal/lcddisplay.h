#ifndef __LCDDISPLAY_H__

#define __LCDDISPLAY_H__

void lcd_show(char* buffer, int size);
void lcd_putc(char c);
void lcd_clear();
void lcd_line_clear();
void lcd_light(int ison);
void lcd_gotoxy(int x, int y);
void lcd_cur_left();
void lcd_cur_right();
void lcd_cur_up();
void lcd_cur_down();

#endif // __LCDDISPLAY_H__

#include <principale.h>

#include <infrared.c>
#include <ds1307.c>
#include <24lc512.c>
#include <aff7seg.c>
#include <ledarray.c>
#include <prieres.c>
#include <date.c>
#include <utility.c>
#include <lcddisplay.c>
#include <mp3.c>
#include <keys.c>

int tmr1_timeout = 2;

void show_day() {
   int dt;
   
   if (!aff7_state) {
      ldarr_off(0);
      ldarr_off(1);
      return;
   }
   
   dt = clk_data[DAY] + 5;
   if (dt > 6) dt -= 7;
   ldarr_show(LED_DAY, 1 << dt);
   ldarr_show(0, dt);
}

void clk_changed(int v) {
   int i;
   
   if (v & CLK_MINUTE_CHANGED) {
      aff7_show_time(clk_data[HOUR], clk_data[MINUTE]);
      if ((clk_data[HOUR] == prayers[PRIERE_FAJR] && clk_data[MINUTE] == prayers[PRIERE_FAJR + 1]) || 
         (clk_data[HOUR] == prayers[PRIERE_DHOHR] && clk_data[MINUTE] == prayers[PRIERE_DHOHR + 1]) || 
         (clk_data[HOUR] == prayers[PRIERE_ASR] && clk_data[MINUTE] == prayers[PRIERE_ASR + 1]) || 
         (clk_data[HOUR] == prayers[PRIERE_MAGHREB] && clk_data[MINUTE] == prayers[PRIERE_MAGHREB + 1]) || 
         (clk_data[HOUR] == prayers[PRIERE_ISHAA] && clk_data[MINUTE] == prayers[PRIERE_ISHAA + 1])) {
         play_mp3();
      }
   }
   
   if (v & CLK_DATE_CHANGED) {
      aff7_show_date(clk_data[DATE], clk_data[MONTH], clk_data[YEAR]);
      show_day();
      
      prieres_load(town_pos);
      aff7_show_prayers(prayers);
   }
}

#int_timer0
void timer0_isr() {
   int v;
   v = clk_read();
   if (v) clk_changed(v);
   if (tmr1_timeout > 0) tmr1_timeout--;
}

void update_display() {
   prieres_load(town_pos);
   location_load(town_pos);
   
   aff7_show_time(clk_data[HOUR], clk_data[MINUTE]);
   aff7_show_date(clk_data[DATE], clk_data[MONTH], clk_data[YEAR]);
   show_day();
   aff7_show_prayers(prayers);
}

void main()
{
   int i;
   int16 st;
   
   delay_ms(5000);
   
   clk_init();
   clk_read();
   if (!clk_is_started()) {
      clk_start();
   }
   setup_timer_0(RTCC_INTERNAL | RTCC_DIV_64);
   
   enable_interrupts(INT_TIMER0);
   enable_interrupts(GLOBAL);
   
   town_pos = clk_get_ville();
   
   update_display();
   
   delay_ms(2000);
   
   lcd_clear();
                 //0123456789ABCDEF0123456789ABC
   strcpy(buffer, "Welcome to      Prayer Caller");
   lcd_show(buffer, 0x1D);
   
   while (1) {   
      if (input(IR_DATA_READY)) {
         disable_interrupts(GLOBAL);
         output_low(IR_RQ_SEND);
         i = fgetc(ir);
         output_high(IR_RQ_SEND);
         enable_interrupts(GLOBAL);
         
         curr_step = handle_key(i);
         if (curr_step != MENU_PRAYER_CALLER) {
            lcd_light(TRUE);         
         } else {
            lcd_light(FALSE);
         }
      }
      
      if (user_event == USER_DATE_CHANGED) {
         DISABLE_INT;
         clk_set_date(dec2bcd(edit_val[0]), dec2bcd(edit_val[1]), dec2bcd(edit_val[2]));
         ENABLE_INT;
      } else if (user_event == USER_TIME_CHANGED) {
         DISABLE_INT;
         clk_set_time(dec2bcd(edit_val[0]), dec2bcd(edit_val[1]));
         ENABLE_INT;
      } else if (user_event == USER_PRAYERS_CHANGED) {
         for (i = 0 ; i < 12 ; i++) { edit_val[i] = dec2bcd(edit_val[i]); }
         DISABLE_INT;
         aff7_show_prayers(edit_val);
         ENABLE_INT;
      } else if (user_event == USER_POWERON_CHANGED) {
         aff7_state = !aff7_state;
      } else if (user_event == USER_TOWN_CHANGED) {
         DISABLE_INT;
         town_pos = edit_val[0];
         clk_set_ville(town_pos);
         ENABLE_INT;
         update_display();
      } else if (user_event == USER_PLAY_SOUND) {
         play_mp3();
         user_event = 0;
      } else if (user_event == USER_STOP_SOUND) {
         stop_mp3();
         user_event = 0;
      }
      
      if (user_event == USER_TIME_CHANGED || user_event == USER_DATE_CHANGED  || 
          user_event == USER_PRAYERS_CHANGED || user_event == USER_POWERON_CHANGED ||
          user_event == USER_TOWN_CHANGED) {
         if (user_event != USER_PRAYERS_CHANGED) 
            update_display();
         user_event = 0;
      }
      
      if (curr_step == MENU_PRAYER_CALLER) {
         if (is_playing) {
            if (tmr1_timeout == 0) {
               state_mp3();
               lcd_light(TRUE);
               i = sprintf(buffer, "Azan Playing    Time : %04ld   ", mp3_pos);
               lcd_gotoxy(0, 0);
               lcd_show(buffer, i);
               st = mp3_pos;
               tmr1_timeout = 2;
            }
            
            if (curr_state == FALSE) {
               lcd_light(FALSE);
               show_menu();
               is_playing = FALSE;
            }
         }
      }
   }
}


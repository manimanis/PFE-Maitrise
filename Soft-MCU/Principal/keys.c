#include "keys.h"

char last_key = 0, 
     last_key_count = 0,
     key_ready = FALSE;
     
int  dec_val,
     dec_min,
     dec_max,
     dec_count;
int  edit_val[12];     

int curr_step = MENU_PRAYER_CALLER;
int curr_cmd = 0;

int user_event = 0;

void show_menu() {
   int16 state;
   int size;
   
   if (curr_step == MENU_PRAYER_CALLER)
   {
      // 123456789ABCDEF0123456789ABCD
      strcpy(buffer, "Welcome to      Prayer Caller");
      lcd_clear();
      lcd_show(buffer, 0x1D);
      
   }
   else if (curr_step == MENU_CONFIG_HOURS)
   {
      if (curr_cmd == 0) {
                       // 0123456789ABCDEF01  234
         sprintf(buffer, "REGLAGE HEURE   %02d:%02d", bcd2dec(clk_data[HOUR]), bcd2dec(clk_data[MINUTE]));
         lcd_clear();
         lcd_show(buffer, 0x15);
      } else if (curr_cmd == 1 || curr_cmd == 2) {
         lcd_gotoxy(0, 1);
         sprintf(buffer, "%02d:%02d", edit_val[0], edit_val[1]);
         lcd_show(buffer, 0x05);
         lcd_gotoxy((curr_cmd == 1) ? 0 : 3, 1);
      } 
   }
   else if (curr_step == MENU_CONFIG_DATE)
   {
      if (curr_cmd == 0) {
                      //  0123456789ABCDEF01  234  567
         sprintf(buffer, "REGLAGE DATE    %02d/%02d/%02d", bcd2dec(clk_data[DATE]), bcd2dec(clk_data[MONTH]), bcd2dec(clk_data[YEAR]));
         lcd_clear();
         lcd_show(buffer, 0x18);
      } else if (curr_cmd == 1 ||curr_cmd == 2 || curr_cmd == 3) {
         lcd_gotoxy(0, 1);
         sprintf(buffer, "%02d/%02d/%02d", edit_val[0], edit_val[1], edit_val[2]);
         lcd_show(buffer, 0x08);
         if (curr_cmd == 1) lcd_gotoxy(0, 1);
         else if (curr_cmd == 2) lcd_gotoxy(3, 1);
         else lcd_gotoxy(6, 1);
      } 
   }
   else if (curr_step == MENU_CONFIG_PRAYERS)
   {
      if (curr_cmd == 0) {
         lcd_clear();
         //  0123456789ABCDE
         sprintf(buffer, "REGLAGE PRIERES");
         lcd_show(buffer, 0x0F);
      } else if (curr_cmd == 1 || curr_cmd == 2) {
                        //012345678  9AB
         sprintf(buffer, "FAJR   %02d:%02d", edit_val[0], edit_val[1]);
      } else if (curr_cmd == 3 || curr_cmd == 4) {
                        //012345678  9AB
         sprintf(buffer, "SHURUQ %02d:%02d", edit_val[2], edit_val[3]);
      } else if (curr_cmd == 5 || curr_cmd == 6) {
                        //012345678  9AB
         sprintf(buffer, "THUHR  %02d:%02d", edit_val[4], edit_val[5]);;
      } else if (curr_cmd == 7 || curr_cmd == 8) {
                        //012345678  9AB
         sprintf(buffer, "ASR    %02d:%02d", edit_val[6], edit_val[7]);
      } else if (curr_cmd == 9 || curr_cmd == 10) {
                        //012345678  9AB
         sprintf(buffer, "MAGHR. %02d:%02d", edit_val[8], edit_val[9]);
      } else if (curr_cmd == 11 || curr_cmd == 12) {
                        //012345678  9AB
         sprintf(buffer, "ISHAA  %02d:%02d", edit_val[10], edit_val[11]);   
      }
      if (curr_cmd > 0) {
         lcd_gotoxy(0, 1);
         lcd_show(buffer, 0x0c);
         lcd_gotoxy(((curr_cmd & 1) == 1) ? 7 : 10, 1);
      }
   }
   else if (curr_step == MENU_CONFIG_MP3)
   {
      if (curr_cmd == 0) {
                      //  0123456789ABCDEF01  234  567
         sprintf(buffer, "DIFFUSER AZAN");
         lcd_clear();
         lcd_show(buffer, 0x0D);
      } else if (curr_cmd == 1) {
                      //  0123456789ABCDEF01  234  567
         sprintf(buffer, "PLAY");
         lcd_gotoxy(0, 1);
         lcd_show(buffer, 0x04);
      } else if (curr_cmd == 2) {
                      //  0123456789ABCDEF01  234  567
         sprintf(buffer, "STOP");
         lcd_gotoxy(0, 1);
         lcd_show(buffer, 0x04); 
      }
   }
   else if (curr_step == MENU_CONFIG_TOWN) 
   {
      if (curr_cmd >= 0) 
      {
         if (curr_cmd == 0) {
            location_load(town_pos);
            edit_val[0] = town_pos;
         } else {
            location_load(edit_val[0]);
         }
                        //0123456789ABCD
         sprintf(buffer, "CONF. VILLE %02d", edit_val[0]);
         lcd_clear();
         lcd_show(buffer, 0x0E);
         size = sprintf(buffer, "%s", town_info.ville);
         lcd_gotoxy(0, 1);
         lcd_show(buffer, size);
         if (curr_cmd == 1) lcd_gotoxy(0, 1);
      }
   }
}

void init_bounds() {
   if (curr_step == MENU_CONFIG_HOURS) {
      if (curr_cmd == 1) {
         dec_min = 0;
         dec_max = 23;
      } else if (curr_cmd == 2) {
         dec_min = 0;
         dec_max = 59;
      }
   } else if (curr_step == MENU_CONFIG_DATE) {
      if (curr_cmd == 1) {
         dec_min = 1;
         dec_max = 31;
      } else if (curr_cmd == 2) {
         dec_min = 1;
         dec_max = 12;
      } else if (curr_cmd == 3) {
         dec_min = 0;
         dec_max = 99;
      }
   } else if (curr_step == MENU_CONFIG_PRAYERS) {
      if (curr_cmd > 0) {
         if ((curr_cmd & 1) == 1) {
            dec_min = 0;
            dec_max = 23;
         } else {
            dec_min = 0;
            dec_max = 59;
         }
      }
   } else if (curr_step == MENU_CONFIG_TOWN) {
      if (curr_cmd == 1) {
         dec_min = 0;
         dec_max = 12;
      }
   }
}

int handle_key(int key) {   
   int i;
   if (key == last_key)
   {
      last_key_count++;
   }
   else
   {
      last_key = key;
      last_key_count = 1;
   }
   
   key_ready = (last_key_count == 3);
   
   if (!key_ready) return curr_step;
   
   if (key == KEY_MUTE) {
      last_key_count = 0;
      stop_mp3();
      lcd_light(FALSE);
      curr_cmd = 0;
      curr_step = MENU_PRAYER_CALLER;
      show_menu();
   } else if (key == KEY_ONOFF) {
      last_key_count = 0;
      user_event = USER_POWERON_CHANGED;
   } else if (key == KEY_MENU) {
      last_key_count = 0;
      curr_step++;
      if (curr_step >= MENU_COUNT) curr_step = 0;
      curr_cmd = 0;
      dec_val = 0;
      if (curr_step == MENU_CONFIG_HOURS) {         
         edit_val[0] = bcd2dec(clk_data[HOUR]);
         edit_val[1] = bcd2dec(clk_data[MINUTE]);
         dec_count = 2;
      } else if (curr_step == MENU_CONFIG_DATE) { 
         edit_val[0] = bcd2dec(clk_data[DATE]);
         edit_val[1] = bcd2dec(clk_data[MONTH]);
         edit_val[2] = bcd2dec(clk_data[YEAR]); 
         dec_count = 3;
      } else if (curr_step == MENU_CONFIG_TOWN) {
         edit_val[0] = town_pos;
         dec_count = 1;
      } else if (curr_step == MENU_CONFIG_PRAYERS) {
         for (i = 0 ; i < 12 ; i++) edit_val[i] = bcd2dec(prayers[i]);
         dec_count = 12;
      } else if (curr_step == MENU_CONFIG_MP3) {
         dec_count = 2;
      }
      init_bounds();
      show_menu();
   } else if (key == KEY_OK) {
      last_key_count = 0;
      if (curr_cmd == 0) {
         curr_cmd = 1;
         init_bounds();
      } else {
         if (curr_step == MENU_CONFIG_HOURS)        user_event = USER_TIME_CHANGED;
         else if (curr_step == MENU_CONFIG_DATE)    user_event = USER_DATE_CHANGED; 
         else if (curr_step == MENU_CONFIG_PRAYERS) user_event = USER_PRAYERS_CHANGED;
         else if (curr_step == MENU_CONFIG_TOWN)    user_event = USER_TOWN_CHANGED;
         else if (curr_step == MENU_CONFIG_MP3) {
            if (curr_cmd == 1)
               user_event = USER_PLAY_SOUND;
            else
               user_event = USER_STOP_SOUND;
         }
         curr_cmd = 0;
         curr_step = MENU_PRAYER_CALLER;
      }
      show_menu();
//!      if (curr_step == MENU_CONFIG_MP3) {
//!         if (curr_cmd == 0) {
//!            last_key_count = 0;
//!            curr_cmd = 1;
//!            play_mp3();
//!            show_menu();
//!         } else if (curr_cmd == 1) {
//!            last_key_count = 0;
//!            curr_cmd = 2;
//!            stop_mp3();
//!            show_menu();
//!         } else if (curr_cmd == 2) {
//!            last_key_count = 0;
//!            curr_cmd = 1;
//!            play_mp3();
//!            show_menu();
//!         }
//!      } 
   } else if (key == KEY_RIGHT) {
      if (curr_cmd > 0) {
         last_key_count = 0;
         curr_cmd++;
         if (curr_cmd > dec_count) curr_cmd = 1;
         dec_val++;
         if (dec_val >= dec_count) dec_val = 0;
         init_bounds();
         show_menu();
      }
   } else if (key == KEY_LEFT) {
      if (curr_cmd > 0) {
         last_key_count = 0;
         curr_cmd--;
         if (curr_cmd < 1) curr_cmd = dec_count;
         dec_val--;
         if (dec_val == 0xff) dec_val = dec_count - 1;
         init_bounds();
         show_menu();
      } 
   } else if (key == KEY_UP) {
      if (curr_cmd > 0) {
         last_key_count = 0;
         edit_val[dec_val] = edit_val[dec_val] + 1;
         if (edit_val[dec_val] > dec_max) edit_val[dec_val] = dec_min;
         show_menu();
      }
   } else if (key == KEY_DOWN) {
      if (curr_cmd > 0) {
         last_key_count = 0;
         edit_val[dec_val] = edit_val[dec_val] - 1;
         if (edit_val[dec_val] == 0xff || edit_val[dec_val] < dec_min) edit_val[dec_val] = dec_max;
         show_menu();
      }
   }
   
   return curr_step;
}


#include "ds1307.h"
#include "date.h"
#include "utility.h"

int8 clk_last[7], 
     clk_data[7];

int clk_event() {
   int change;
   
   change = CLK_NO_CHANGE;
   if (clk_last[YEAR] != clk_data[YEAR])        change |= CLK_YEAR_CHANGED;
   if (clk_last[MONTH] != clk_data[MONTH])      change |= CLK_MONTH_CHANGED;
   if (clk_last[DATE] != clk_data[DATE])        change |= CLK_DATE_CHANGED;
   if (clk_last[HOUR] != clk_data[HOUR])        change |= CLK_HOUR_CHANGED;
   if (clk_last[MINUTE] != clk_data[MINUTE])    change |= CLK_MINUTE_CHANGED;
   if (clk_last[SECOND] != clk_data[SECOND])    change |= CLK_SECOND_CHANGED;
   return change;
}

void clk_init() {
   memset(clk_last, 0, sizeof(clk_last));
   memset(clk_data, 0, sizeof(clk_data));
}

void clk_start() {
   bit_clear(clk_data[SECOND], CLK_HALT_BIT);
   clk_write();
}

void clk_stop() {
   bit_set(clk_data[SECOND], CLK_HALT_BIT);
   clk_write();
}

int  clk_is_started() {   
   return (!bit_test(clk_data[SECOND], CLK_HALT_BIT));
}

void clk_set_time(int hr, int mn) {
   clk_data[HOUR] = hr;
   clk_data[MINUTE] = mn;
   clk_data[SECOND] = 0;
   
   clk_write();
}

void clk_set_date(int dt, int mth, int yr) {
   clk_data[DATE] = dt;
   clk_data[MONTH] = mth;
   clk_data[YEAR] = yr;
   clk_data[DAY] = date_jds(date_nbj(bcd2dec(dt), bcd2dec(mth), bcd2dec(yr)));
   
   clk_write();
}

int clk_read() {
   int i;   
   
   memcpy(clk_last, clk_data, sizeof(clk_data));
   
   i2c_start();
   i2c_write(CLK_ADDRESS);
   i2c_write(0);
   i2c_start();
   i2c_write(CLK_ADDRESS_RD);
   
   for (i = 0; i < 7 ; i++) {
      clk_data[i] = i2c_read(i != 6);
   }
   
   i2c_stop();
   
   return clk_event();
}

void clk_write() {
   int i;
   
   i2c_start();
   i2c_write(CLK_ADDRESS);
   i2c_write(0);
   
   for (i = 0; i < 7 ; i++) {
      i2c_write(clk_data[i]);
   }
   
   i2c_stop();
}

int16 clk_days() {
   int16 dy;
   
   dy = 0;
   
   if (clk_data[MONTH] > 1) dy += 31;
   if (clk_data[MONTH] > 2) dy += 29;
   if (clk_data[MONTH] > 3) dy += 31;
   if (clk_data[MONTH] > 4) dy += 30;
   if (clk_data[MONTH] > 5) dy += 31;
   if (clk_data[MONTH] > 6) dy += 30;
   if (clk_data[MONTH] > 7) dy += 31;
   if (clk_data[MONTH] > 8) dy += 31;
   if (clk_data[MONTH] > 9) dy += 30;
   if (clk_data[MONTH] > 0x10) dy += 31;
   if (clk_data[MONTH] > 0x11) dy += 30;
   if (clk_data[MONTH] > 0x12) dy += 31;
   
   dy += bcd2dec(clk_data[DATE]) - 1;
   
   return dy;
}

void clk_set_ville(int ville) {
   i2c_start();
   i2c_write(CLK_ADDRESS);
   i2c_write(CLK_TOWN_LOCATION);
   
   i2c_write(ville);
   
   i2c_stop();
}

int  clk_get_ville() {
   int pos ;
   i2c_start();
   i2c_write(CLK_ADDRESS);
   i2c_write(CLK_TOWN_LOCATION);
   i2c_start();
   i2c_write(CLK_ADDRESS_RD);
   
   pos = i2c_read(FALSE);
   
   i2c_stop();
   
   return pos;
}


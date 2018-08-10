#ifndef __DS1307_H__

#define __DS1307_H__

#define CLK_ADDRESS        0xD0
#define CLK_ADDRESS_RD     0xD1
#define CLK_HALT_BIT       7
#define CLK_AM_BIT         5

#define SECOND             0
#define MINUTE             1
#define HOUR               2
#define DAY                3
#define DATE               4
#define MONTH              5
#define YEAR               6

#define CLK_SECOND_CHANGED 1
#define CLK_MINUTE_CHANGED 2
#define CLK_HOUR_CHANGED   4
#define CLK_DATE_CHANGED   8
#define CLK_MONTH_CHANGED  16
#define CLK_YEAR_CHANGED   32
#define CLK_ALL_CHANGED    255
#define CLK_NO_CHANGE      0

#define CLK_TOWN_LOCATION 8

int clk_event();

void clk_start();
void clk_stop();
int  clk_is_started();

void clk_set_time(int hr, int mn);
void clk_set_date(int dt, int mth, int yr);

int  clk_read();
void clk_write();

int16 clk_days();

void clk_set_ville(int ville);
int  clk_get_ville();

#endif //__DS1307_H__

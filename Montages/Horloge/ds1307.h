#ifndef __DS1307_H__

#define __DS1307_H__

#define CLK_ADDRESS        0xD0
#define CLK_ADDRESS_RD     0xD1
#define CLK_HALT_BIT       7
#define CLK_AM_BIT         5

#define SECOND             0
#define MINUTE             1
#define HOUR               2

#define CLK_SECOND_CHANGED 1
#define CLK_MINUTE_CHANGED 2
#define CLK_HOUR_CHANGED   4
#define CLK_ALL_CHANGED    7
#define CLK_NO_CHANGE      0

#define CLK_TOWN_LOCATION 8

int clk_event();

void clk_start();
void clk_stop();
int  clk_is_started();

void clk_set_time(int hr, int mn);

int  clk_read();
void clk_write();

#endif //__DS1307_H__
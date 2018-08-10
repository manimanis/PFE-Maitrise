#ifndef __PRIERES_H__

#define __PRIERES_H__

#define PRIERE_FAJR        0
#define PRIERE_CHOUROUK    2
#define PRIERE_DHOHR       4
#define PRIERE_ASR         6
#define PRIERE_MAGHREB     8
#define PRIERE_ISHAA       10

struct struct_location {
   char pays[16];
   char region[16];
   char ville[16];
   int16 lg_deg;
   int lg_min;
   int16 lg_sec;
   char lg_sens;
   int16 la_deg;
   int la_min;
   int16 la_sec;
   char la_sens;
   int gmt;
   int dst;
   int method;
} ;

void prieres_load(int town_pos);
void location_load(int town_pos);

#endif // __LEDARRAY_H__

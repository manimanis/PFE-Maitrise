#include <date.h>

int date_isleap(int yy) {
   return ((yy & 0x03) == 0);
}

int16 date_nbj(int jj, int mm, int aa) {
   int16 nbj;
   
   nbj = jj;
   if (mm > 1) nbj += 31;
   if (mm > 2) {
      nbj += 28;
      nbj += date_isleap(aa);
   }
   if (mm > 3) nbj += 31;
   if (mm > 4) nbj += 30;
   if (mm > 5) nbj += 31;
   if (mm > 6) nbj += 30;
   if (mm > 7) nbj += 31;
   if (mm > 8) nbj += 31;
   if (mm > 9) nbj += 30;
   if (mm > 10) nbj += 31;
   if (mm > 11) nbj += 30;
   
   nbj += 365 * aa;
   nbj += (aa - 1) / 4; // jours des années bissextiles
   
   return nbj;
}

int date_jds(int16 val) {
   return (val % 7 + 1);
}

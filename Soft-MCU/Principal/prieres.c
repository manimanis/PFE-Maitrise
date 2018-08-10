#include "prieres.h"

int town_pos = 0;
int prayers[12];

struct struct_location town_info;

void prieres_load(int town_pos) {
   int16 days;
   int16 address;
   
   days = clk_days();   
   address = (int16)38 * town_pos + days / 10 + 1;
   mem_read_page(MEM_ADDRESS1, address, buffer);
   memcpy(prayers, buffer + (days % 10) * 12, 12);
}

void location_load(int town_pos) {
   int i;
   int16 address;
   
   address = (int16)38 * town_pos;
   mem_read_page(MEM_ADDRESS1, address, buffer);
   memcpy(&town_info, buffer, sizeof(town_info));
   for (i = 0; i < 16 ; i++) {
      if (town_info.pays[i] == 0xFF) town_info.pays[i] = 0;
      if (town_info.region[i] == 0xFF) town_info.region[i] = 0;
      if (town_info.ville[i] == 0xFF) town_info.ville[i] = 0;
   }
}

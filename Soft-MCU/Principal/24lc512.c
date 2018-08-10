#include "24lc512.h"
#include "lcddisplay.h"

int buffer[128];

#define hi(x) (*((int8 *)&x+1))

void mem_read_page(int dev_addr, unsigned int16 page, char* buffer) {
   int i;
   unsigned int16 address;
   
   address = page << 7;
   
   i2c_start();
   i2c_write(dev_addr);
   i2c_write(hi(address));
   i2c_write(address);
   i2c_start();
   i2c_write(dev_addr | 1);
   
   for (i = 0 ; i < 128 ; i++) {
      buffer[i] = i2c_read(i != 127);
   }
   
   i2c_stop();
}

void mem_write_page(int dev_addr, unsigned int16 page, char* buffer) {
   int i;
   
   i2c_start();
   i2c_write(dev_addr);
   i2c_write(page >> 1);
   i2c_write((page & 1) << 7);
   
   for (i = 0 ; i < 128 ; i++) {
      i2c_write(buffer[i]);
   }
   
   i2c_stop();
   
   do {
      i2c_start();
      i = i2c_write(dev_addr);
   } while (i == 1);
   
   i2c_stop();
}

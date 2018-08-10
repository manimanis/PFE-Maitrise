#ifndef __24LC512_H__

#define __24LC512_H__

#define MEM_ADDRESS1          0xA0
#define MEM_ADDRESS2          0xA2

void mem_read_page(int dev_addr, unsigned int16 page, char* buffer);
void mem_write_page(int dev_addr, unsigned int16 page, char* buffer);

#endif // __24LC512_H__

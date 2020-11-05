#each SA contains two keys, for a total of four

declare -a keys
for i in {1..4}; do
  # keys 1 and 3 are message authenitcation codes, keys 2 and 4 are for encryption
  keys[i]=$(xxd -p -l 32 -c 32 /dev/random)
done

#each SA requires an SPI

declare -a spi
for i in {1..2}; do
  spi[i]=$(xxd -p -l 4 /dev/random)
done

# ID which links the SA and SPD

declare -a reqid
for i in {1..2}; do
  reqid[i]=$(xxd -p -l 4 /dev/random)
done
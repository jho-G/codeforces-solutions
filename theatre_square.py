n,m,a=map(int,input().split())

tile_length=(n+a-1)//a
tile_width=(m+a-1)//a

number_of_tiles=tile_length*tile_width
print(number_of_tiles)
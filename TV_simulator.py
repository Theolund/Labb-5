from TV import Tv
tvobjects=[]

def read_file():
    with open("allatv.txt","r") as file:
         for line in file:
            tv_name,max_channel,current_channel,max_volume,current_volume=line.strip().split(",")
            tvobjects.append(Tv(tv_name, int(max_channel),int(current_channel),int(max_volume),int(current_volume)))
    return tvobjects

def write_file():
    with open("allatv.txt","w") as file:
        for tv in tvobjects:
            file.write(tv.str_for_file()+"\n")

tvlista=read_file()
for tv in tvlista:
    print(tv)

tvobjects[0].change_channel(1)
for tv in tvlista:
    print(tv)

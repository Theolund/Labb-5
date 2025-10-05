class Tv:
    def __init__(self, tv_name, current_volume, current_channel, max_volume, max_channel):
        self.tv_name=tv_name
        self.current_volume=current_volume
        self.current_channel=current_channel
        self.max_volume=max_volume
        self.max_channel=max_channel
    
    def change_channel(self,new_channel):
        if new_channel>self.max_channel or new_channel<=1:
            return False
        else:
            return True

    def increase_volume(self):
        if self.current_volume==self.max_volume:
            return False
        else:
            return True
    
    def decrease_volume(self):
        if self.current_volume==0:
            return False
        else:
            return True
        
    def __str__(self):
       info=f"{self.tv_name}, kanal {self.current_channel}, ljudnivå {self.current_volume}"
       return info
    
    def str_for_file(self):
        info=str(f"{self.tv_name},{self.max_channel},{self.current_channel},{self.max_channel},{self.current_volume}")
        return info

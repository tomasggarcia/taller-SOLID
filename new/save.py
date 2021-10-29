class Save():
    def save_in_file(self, file, string):
        file = open(file,'w') 
        file.write(string)
        file.close()
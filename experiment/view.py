from model import Model

class View():
    def __init__(self):
        pass

    def showAll(self, list):
        pass
        # print('In our db we have %i users. Here they are:' % len(list))
        # for item in list:
        #     print(item.name())

    def start(self):
        # pass
        print('MVC - the simplest example')
        print('Do you want to see everyone in my db?[y/n]')

    def end(self):
        pass
        # print('Goodbye!')
    
if __name__ == "__main__":
    #running controller function
    # Controller.start()
    # View.start()
    v = View()
    v.start()
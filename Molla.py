import random

salty_list = [['prawn shumai, £6.50'],
        ['chicken dumpling, £5.50'],
        [ 'soft tofu salad, £6.80'],
        [ 'avocado seaweed salad, £7.20'],
        ['kimchi pancake, £8.70'],
        ['tiger prawn salad, £7.80'],
        ['bbq beef roll, £6.80']]
         
import random 
spicy_list = [['kimchi rice ball, £5.20',],
            [ 'kimchi fried rice, £8.50',],
            ['spicy stir fried squid, £13.50'],
            ['tofu kimchi, £9.80'],
            ['chive pancake, £9.00'],
            ['tteok-bokki, £8.80'],
            ['cheese tteok-bokki, £10.50']]

salty_list = random.choice(salty_list)
spicy_list = random.choice(spicy_list)

# flavour profile


while True:
        print ('are you in the mood for something salty or spicy?')
        mood = input ()
        if mood == "salty":
            print (salty_list)
            quit()        
        elif mood == "spicy":
            print (spicy_list)
            quit()
        else:
            print ("That's not a flavour profile on our menu. Please choose salty or spicy.")
            continue           
         
         





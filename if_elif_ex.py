#Assining college on rank based
rank = int(input('Enter your rank'))
if rank <= 1000:
    print ('You got college1')
elif rank >1000 and rank <= 10000:
    print ('You got college2')
elif rank > 10000 and rank <=40000:
    print ('You got college3')
else:
    print ('Better luck next time..')
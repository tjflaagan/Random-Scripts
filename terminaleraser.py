import sys, time

print ('And now for something completely different ...')
time.sleep(0.5)

msg = 'I am going to erase this line from the console window.'
sys.stdout.write(msg); sys.stdout.flush()
time.sleep(1)

sys.stdout.write('\r' + ' '*len(msg))
sys.stdout.flush()
time.sleep(0.5)

print('\rdid I succeed?')
time.sleep(1)
import time
import datetime

# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
#Oct 21 2022$
scientific = '{:.2e}'.format(time.time())
day = datetime.date(time.gmtime(0)[0], time.gmtime(0)[1], time.gmtime(0)[2]).strftime('%B') 
print("Seconds since", day, time.gmtime(0)[2],",", time.gmtime(0)[0], ":", "{:,.4f}".format(time.time()), "or", scientific, "in scientific notation")
print(time.strftime("%b %d %Y", time.gmtime(time.time())))

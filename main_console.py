import getpos, gpx_builder

# ip = input("Insert the destination's ip direction: ")
# jumps = int(input("Insert the number of jumps the trace will do before stopping: "))

# TEST DATA
iplist = ["94.142.103.97", "176.52.249.37", "213.140.35.105", "94.142.107.106", "184.105.65.234", "184.105.223.193",
          "206.81.81.39", "205.220.212.35", "155.254.18.14"]

gpx = gpx_builder.gpx_builder(getpos.geodata(iplist))

# file = open("{}.gpx.".format(iplist[0]), 'w')
# file.write(gpx_builder.gpx_builder(getpos.geodata(iplist)))
# file.close()

gpx.write(open("{}.gpx".format(iplist[0]), "wb"))

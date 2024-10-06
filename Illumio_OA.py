import sys

def readfileandMap(log_file, map_file,output_tag_file='output_tags_count.csv',output_port_protocol_file='output_port_protocol.csv'):

  protocol_num_map = {}
  with open("./protocols.txt","r") as file:
    for line in file:
      line = line.strip()
      line = line.split()
      if len(line)<2:
        continue
      protocol_num_map[line[0]] = line[1].lower()

  column_check1 = "version"
  column_check2 = "account-id"
  dstport = {}
  with open(log_file,"r") as file:
    for line in file:
      line = line.strip()
      if column_check1 in line and column_check2 in line:
        continue
      line = line.split()
      if line[7] in protocol_num_map:
        dstport[line[6]+':'+protocol_num_map.get(line[7])] = dstport.get(line[6]+':'+protocol_num_map.get(line[7]),0) + 1
      else:
        continue


  map_column_check1 = "dstport"
  map_column_check2 = "protocol"
  dst_protocol_map = {}

  with open(map_file,"r") as file:
    for line in file:
      line = line.strip()
      if map_column_check1 in line and map_column_check2 in line:
        continue
      line = line.split(",")
      if len(line)<2:
        continue
      dst_protocol_map[line[0]+':'+line[1].lower()] = line[2]


  tag_count = {}
  for key in dstport:
    if key in dst_protocol_map:
      tag = dst_protocol_map[key]
      tag_count[tag] = tag_count.get(tag,0) + dstport[key]
    else:
      tag_count['Untagged'] = tag_count.get('Untagged',0) + dstport[key]

  # Writing data to a plain text file in CSV format
  with open(output_tag_file, mode='w') as file:
    file.write('Tag,Count'+'\n')
    for key in tag_count:
        # Join each element of the row with commas and write to the file
        file.write(key+',' + str(tag_count.get(key)) + '\n')
  print("Data written to output_tag file")

  # Writing data to a plain text file in CSV format
  with open(output_port_protocol_file, mode='w') as file:
    file.write('Port,Protocol,Count'+'\n')
    for key in dstport:
        dstPort_protocol = key.split(':')
        port = dstPort_protocol[0]
        protocol = dstPort_protocol[1]
        # Join each element of the row with commas and write to the file
        file.write(port +','+ protocol +',' + str(dstport.get(key)) + '\n')
  print("Data written to output_port_protocol file")

if __name__ == "__main__":
  readfileandMap(sys.argv[1],sys.argv[2])
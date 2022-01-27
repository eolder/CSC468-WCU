import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
# Create a XenVM
node = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
node.routable_control_ip = "true"

updstr = "sudo apt install -y"
packages = [
  "apache2",
  "htop",
  "tmux",
]
for x in packages:
  updstr += " " + x

node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update && sudo apt upgrade -y"))
node.addService(rspec.Execute(shell="/bin/sh", command=updstr))
node.addService(rspec.Execute(shell="/bin/sh", command="sudo systemctl status apache2"))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()

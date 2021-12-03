#!/bin/perl
## Synopsis 
## THE SNMP REQUESTS

## THE SNMP SUBS
## Débit
sub datarate{
    ## to reDO
        system("$DIR_snmpscripts/datarate.sh >> $DIR_result/dataTEST");
}

## Mémoire totales et utilisées
sub memories{
    my ($timer) = &read_cmd("date +Date:%FTime:%T");
    my ($totalram) = &read_cmd("snmpget -Oqv -v2c -c alluser  $server_ip 1.3.6.1.4.1.2021.4.5.0 | cut -d \" \" -f1");
    #print "Total ram for  $server_name  :  $totalram at $timer \n";
    my ($usedram) = &read_cmd("snmpget -Oqv -v2c -c alluser  $server_ip 1.3.6.1.4.1.2021.4.6.0 | cut -d \" \" -f1");
    
    #system("$DIR_snmpscripts/memory.sh >> $DIR_result/memoryTEST");
    #Ecriture du bloc xml
    &xml_bloc("ramUsage",
		(
			'TotalRam' => $totalram,
			'UsedRam' => $usedram,
			'TestDate' => $timer,
            'Server'  => $server_name
		)
	);	
}

sub swaps{
    my ($timer) = &read_cmd("date +Date:%FTime:%T");
    my ($swapusage) = &read_cmd("snmpget -Oqv -v2c -c alluser  $server_ip 1.3.6.1.4.1.2021.4.4.0 | cut -d \" \" -f1");
    #Ecriture du bloc xml
    &xml_bloc("SwapSize",
		(
			'SwapUsage' => $swapusage,
			'TestDate' => $timer,
            'Server'  => $server_name
		)
	);	
}

## Utilisation du CPU
sub cpuses{
    ## to reDO
    my ($timer) = &read_cmd("date +Date:%FTime:%T");
    my ($cpunonusage) = &read_cmd("snmpget -Oqv -v2c -c alluser  $server_ip .1.3.6.1.4.1.2021.11.11.0 | cut -d \" \" -f4");
    $thehundred = "100";
    $cpusage = $thehundred - $cpunonusage;
    #Ecriture du bloc xml
    &xml_bloc("CpuUse",
		(
			'CpuUsage' => $cpusage,
			'TestDate' => $timer,
            'Server'  => $server_name
		)
	);	
}



## THE END
1;
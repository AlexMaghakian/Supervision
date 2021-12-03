#!/bin/perl
## Synopsis 
## Snmp Request Scheduler

## python : flask & bootstrap (css) ; pandas pour graphique


## Variables
$DIR_bin="/Project_Monitoring/bin";
$DIR_snmpscripts="/Project_Monitoring/scripts_snmp";
$DIR_conf="/Project_Monitoring/conf";
$DIR_result="/Project_Monitoring/results";
$DIR_log="/Project_Monitoring/logs";

## List of tags :
## generic
## cpu
## network

## Loading other pl libraries/scripts
require("$DIR_bin/lib.pl");
require("$DIR_bin/snmplibs.pl");

## Logging the program
#my $LOG_date=&time_string;
#$LOG_date=~s/[,\:\-]//g;
#$LOG_date=~s/[\s]/_/g;


## Call of subs...
#&plannedjob;


## Script Calling 
$tagtoparse="";
&scripts_calls;
sub scripts_calls{
    my ($timer)=&read_cmd("date +%F_%T");
    my ($script_turn)=&read_cmd("cat $DIR_conf/turn");
	if($script_turn == 1 ){
		## Time to do generic check
        open(XML,">$DIR_result/generic_$timer.xml");
        &open_tag("results");
        $tagtoparse="generic";
        &open_tag("generic");
        ## Selection of servers concerned by this this set of test (and get name and ip adress)


        &server_parse;

        ## call of sub (done for each server selected before end)
        #&memories;

        # conf/turn increment
        my ($check_cmd)&read_cmd(" echo \"2\" > $DIR_conf/turn | echo $? ");
        &close_tag("generic");
	}
	if($script_turn == 2 ){
		## Time to do cpu 
        open(XML,">$DIR_result/cpu_$timer.xml");
        &open_tag("results");
        $tagtoparse="cpu";
        &open_tag("cpu");
        ## Selection of servers concerned by this this set of test (and get name and ip adress)

        &server_parse;

        ## call of sub (done for each server selected before end)
      #  &cpu;

        # conf/turn increment
        my ($check_cmd)&read_cmd(" echo \"3\" > $DIR_conf/turn | echo $? ");
        &close_tag("cpu");
	}    
    if($script_turn == 3 ){
		## Time to do network check
        open(XML,">$DIR_result/network_$timer.xml");
        &open_tag("results");
        $tagtoparse="network";
        &open_tag("network");
        ## Selection of servers concerned by this this set of test (and get name and ip adress)


        &server_parse;
        ## call of sub (done for each server selected before end)
        &datarate;

        # conf/turn increment
        my ($check_cmd)&read_cmd(" echo \"1\" > $DIR_conf/turn | echo $? ");
        &close_tag("network");	
	}    
    &close_tag("results");	
    close(XML);
}






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

$tagtoparse="";
## Script Calling 
#$tagtoparse="";
&scripts_calls;
sub scripts_calls{
    my ($timer)=&read_cmd("date +%F_%T");
    my ($script_turn)=&read_cmd("cat $DIR_conf/turn");
    
    my @TAG_LIST=&read_cmd("cat $DIR_conf/taglist");
	foreach $tagtoparse (@TAG_LIST) {
        print   "found $tagtoparse in /conf/taglist \n";
        system("mv $DIR_result/$tagtoparse* $DIR_result/FormerResults");
        ## Time to do generic check
        open(XML,">$DIR_result/$tagtoparse\_$timer.xml");
        &open_tag("results");
        &open_tag("$tagtoparse");
        &server_parse;
        &close_tag("$tagtoparse");
        &close_tag("results");	
        close(XML);
    }

    # conf/turn increment
    #my ($check_cmd)&read_cmd(" echo \"1\" > $DIR_conf/turn | echo $? ");
  

}

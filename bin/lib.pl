#!/bin/perl
## Synopsis
## Founctions and tools used by the scheduler


sub read_cmd {

    my $CMD=$_[0];
    # Chargement du resultat de la commande dans un tableau
    open(CMDHANDLE,"$CMD |") or die("Can't pipe $CMD: $!");
    my @CMD_res=<CMDHANDLE>;
    close(CMDHANDLE);
     # Supprime saut de ligne tabulations et espaces contigus

     foreach(@CMD_res){

        chomp;      # suppression du saut de ligne
        s/\t/ /g;       # suppressions des tabulations
        s/ {2,}/ /g;    # les espaces consecutifs reduit a 1 seul espace
        s/^ //;     # suppression de l'espace de debut de ligne 
    }
     return @CMD_res;

}

sub modify_file {
  open(FILE_IN,$ARGV[0]);
  my @contenu = <FILE_IN>;
  close(FILE_IN);

  open(FILE_OUT,">$ARGV[0]");
  foreach my $ligne (@contenu) {
      $ligne =~ s/Arial/Myriad Pro/g;
      $ligne =~ s/œ/oe/g;
      chomp $ligne;
      print FILE_OUT "$ligne\n";
  }
  close(FILE_OUT);
}

## Parsing server list
sub server_parse{
  my @SERVER_LIST=&read_cmd("cat $DIR_conf/serverlist");
	foreach $line (@SERVER_LIST) {
    if (grep /$tagtoparse/, $line){
      print "found $tagtoparse in $line \n";
      #$serverparsed=&read_cmd("echo \"$line\" | awk -F \";\" '{print $2}' ");
      #$serverparsed=&read_cmd("echo $line | cut -d ';' -f1 ");
      #print "server name is $serverparsed \n";
      my @spl = split (';', $line);
      $iterator="1";
      foreach my $info (@spl){
        #print "$info\n";
        if ($iterator==1){ 
          $server_name=$info;
          print "server name : $server_name \n";
        }
        if ($iterator==2){ 
          $server_ip=$info;
          print "server ip : $server_ip \n";
        }
        $iterator=$iterator+1;
      }
      if($tagtoparse eq "generic" ){
        &memories;
        &swaps;
      }elsif($tagtoparse eq "network"){
        print "it\'s $tagtoparse turn\n";
      }elsif($tagtoparse eq "cpu"){
        &cpuses;
      }
    }
  }
}

# Generation d'un tag XML ouvrant de type
#	 <tagA attrA=valA> ou <tagA>
#
sub open_tag {
	my ($root,%attrTAG)=@_;	
	print XML "<".$root; 
	if(scalar keys 	%attrTAG) {
		foreach(keys %attrTAG) {
			print XML " ".$_."="."\"".$attrTAG{$_}."\"";
		}
	}
	print XML ">\n";
}

# Generation d'un tag XML fermant de type
#	 </tagA>
#
sub close_tag {
	my ($root)=@_;	
	print XML "</".$root.">\n"; 
}


# Generation d'un bloc XML de type
#	<tagA>
#	 <tagB>valB</tagB>
#	  .
#	 <tagZ>valZ</tagZ>
#	</tagA>
#
sub xml_bloc {
	my ($bloc,%blocTAG)=@_;
	print XML "\t<".$bloc.">\n";
	foreach (sort keys %blocTAG) {
			print XML "\t <".$_.">".$blocTAG{$_}."</".$_.">\n";	
	}
	print XML "\t</".$bloc.">\n";
}


1;


from parseur import *
from count import *
def create_table():
    tab, root_node=parse_date()
    tab_totalram, root_node2=parse_totalram()
    tab_UsedRam, root_node3=parse_UsedRam()
    tab_Server, root_node5=parse_Server()
    countlxml_TotalRam=count()
    #on stock les valeurs de l'attribut TestDate dans la variable TestDate
    TestDate = root_node.findall("generic/ramUsage/TestDate")
    #on stock les valeurs de l'attribut TotalRam dans la variable TotalRam
    TotalRam = root_node2.findall("generic/ramUsage/TotalRam")
    #on stock les valeurs de l'attribut UsedRam dans la variable UsedRam
    UsedRam = root_node3.findall("generic/ramUsage/UsedRam")
    Server = root_node5.findall("generic/ramUsage/Server")
    for Date in TestDate:
        # Get the value from the attribute 'TestDate'
        tab.append(Date.text)
        #print(tab[0])

    for totalram in TotalRam:
        # Get the value from the attribute 'TotalRam'
        tab_totalram.append(totalram.text)
    for usedram in UsedRam:
    # Get the value from the attribute 'UsedRam'
        tab_UsedRam.append(usedram.text)

    for server in Server:
    # Get the value from the attribute 'UsedRam'
        tab_Server.append(server.text)
    #tableau contenant les valeurs qu'on souhaite afficher
    #creer autant de ligne qu'il y a de balise <countlxml_TotalRam>
    i=0
    #lst = [('RAMusage','date','totalram','usedram')]
    lst=[]
    for i in range(countlxml_TotalRam):
        lst.append(['RAM',tab[i],tab_totalram[i],tab_UsedRam[i],tab_Server[i]])
    return lst
    return y
    return tab[i]
    return tab_totalram
#############################################################
#table swap  
def create_table2():
    tab, root_node=parse_date()
    tab_SwapUsage, root_node4=parse_SwapUsage()
    tab_Server, root_node5=parse_Server()
    countlxml_SwapSize=count2()
    countlxml_SwapUsage=count2()
    countlxml_Server_ram=count()
    #on stock les valeurs de l'attribut TestDate dans la variable TestDate
    TestDate_swap = root_node.findall("generic/SwapSize/TestDate")
    #on stock les valeurs de l'attribut TotalRam dans la variable TotalRam
    SwapUsage = root_node4.findall("generic/SwapSize/SwapUsage")
    #on stock les valeurs de l'attribut UsedRam dans la variable UsedRam
    Server = root_node5.findall("generic/SwapSize/Server")

    for Date_swap in TestDate_swap:
        # Get the value from the attribute 'TestDate_swap'
        tab.append(Date_swap.text)

    for swapusage in SwapUsage:
        # Get the value from the attribute 'SwapUsage'
        tab_SwapUsage.append(swapusage.text)

    for server in Server:
    # Get the value from the attribute 'Server'
        tab_Server.append(server.text)

    #tableau contenant les valeurs qu'on souhaite afficher
    #creer autant de ligne qu'il y a de balise <countlxml_TotalRam>
    y=0
    #lst = [('RAMusage','date','totalram','usedram')]
    lst_swap=[]

    for y in range(countlxml_SwapUsage):
        lst_swap.append(['SWAPusage',tab[y],tab_SwapUsage[y],tab_Server[y]])
    return lst_swap
    return y
    return tab[y]
    return tab_SwapUsage


#########################TABLE CLIENT1 RAM###############################
def create_table_client1_ram():
    tab_client1_date_ram, root_node_client1_date_ram=parse_date_client1_ram()
    tab_client1_UsedRam, root_node_client1_ramUsage=parse_UsedRam_client1()
    tab_client1_totalram, root_node2_client1_totalram=parse_totalram_client1()
    #tree_client1_ramUsage=parse_ramUsage_client1()
    countlxml_ramUsage_client1=count_client1_ram()
    countlxml_ramSize_client1=count_client1_ram()
    TestDate_ram_client1 = root_node_client1_date_ram.findall("generic/ramUsage/TestDate")
    ram_used_client1 = root_node_client1_ramUsage.findall("generic/ramUsage/UsedRam")
    totalram_used_client1 = root_node2_client1_totalram.findall("generic/ramUsage/TotalRam")

    for TotalRam_ram_client1 in totalram_used_client1:
        tab_client1_totalram.append(TotalRam_ram_client1.text)

    for Date_ram_client1 in TestDate_ram_client1:
        tab_client1_date_ram.append(Date_ram_client1.text)

    for ram_used_client1 in ram_used_client1:
        tab_client1_UsedRam.append(ram_used_client1.text)

    #tableau contenant les valeurs qu'on souhaite afficher
    #creer autant de ligne qu'il y a de balise <countlxml_ramUsage_client1>
    a=0
    lst_ram_client1=[]

    for a in range(countlxml_ramUsage_client1):
        lst_ram_client1.append(['ramusage',tab_client1_totalram[a],tab_client1_date_ram[a],tab_client1_UsedRam[a],'Client1'])

    return lst_ram_client1
    return c
    return tab_client1_date
    return tab_client1_ramUsage

#########################TABLE CLIENT1 SWAP###############################
def create_table_client1_swap():
    tab_client1_date_swap, root_node_client1_date_swap=parse_date_client1_swap()
    tab_client1_SwapUsage, root_node_client1_SwapUsage=parse_SwapUsage_client1()
    #tree_client1_SwapUsage=parse_SwapUsage_client1()
    countlxml_SwapUsage_client1=count_client1_swap()
    countlxml_SwapSize_client1=count_client1_swap()
    TestDate_swap_client1 = root_node_client1_date_swap.findall("generic/SwapSize/TestDate")
    SwapUsage_client1 = root_node_client1_SwapUsage.findall("generic/SwapSize/SwapUsage")

    for Date_swap_client1 in TestDate_swap_client1:
        tab_client1_date_swap.append(Date_swap_client1.text)
        print('tab_client1_date', Date_swap_client1)

    for swapusage_client1 in SwapUsage_client1:
        tab_client1_SwapUsage.append(swapusage_client1.text)
        print('tab_client1_SwapUsage', tab_client1_SwapUsage)
    #tableau contenant les valeurs qu'on souhaite afficher
    #creer autant de ligne qu'il y a de balise <countlxml_SwapUsage_client1>
    c=0
    lst_swap_client1=[]

    for c in range(countlxml_SwapUsage_client1):
        lst_swap_client1.append(['SWAPusage',tab_client1_date_swap[c],tab_client1_SwapUsage[c],'Client1'])
        print('lst_swap_client1', lst_swap_client1)
    return lst_swap_client1
    return c
    return tab_client1_date
    return tab_client1_SwapUsage

#########################TABLE CLIENT2 RAM###############################
def create_table_client2_ram():
    tab_client2_date_ram, root_node_client2_date_ram=parse_date_client2_ram()
    tab_client2_UsedRam, root_node_client2_ramUsage=parse_UsedRam_client2()
    tab_client2_totalram, root_node2_client2_totalram=parse_totalram_client2()
    #tree_client2_ramUsage=parse_ramUsage_client2()
    countlxml_ramUsage_client2=count_client2_ram()
    countlxml_ramSize_client2=count_client2_ram()
    TestDate_ram_client2 = root_node_client2_date_ram.findall("generic/ramUsage/TestDate")
    ram_used_client2 = root_node_client2_ramUsage.findall("generic/ramUsage/UsedRam")
    totalram_used_client2 = root_node2_client2_totalram.findall("generic/ramUsage/TotalRam")

    for TotalRam_ram_client2 in totalram_used_client2:
        tab_client2_totalram.append(TotalRam_ram_client2.text)

    for Date_ram_client2 in TestDate_ram_client2:
        tab_client2_date_ram.append(Date_ram_client2.text)

    for ram_used_client2 in ram_used_client2:
        tab_client2_UsedRam.append(ram_used_client2.text)

    #tableau contenant les valeurs qu'on souhaite afficher
    #creer autant de ligne qu'il y a de balise <countlxml_ramUsage_client2>
    d=0
    lst_ram_client2=[]

    for d in range(countlxml_ramUsage_client2):
        lst_ram_client2.append(['ramusage',tab_client2_totalram[d],tab_client2_date_ram[d],tab_client2_UsedRam[d],'Client2'])

    return lst_ram_client2
    return d
    return tab_client2_date
    return tab_client2_ramUsage

#########################TABLE CLIENT2 SWAP###############################
def create_table_client2_swap():
    tab_client2_date_swap, root_node_client2_date_swap=parse_date_client2_swap()
    tab_client2_SwapUsage, root_node_client2_SwapUsage=parse_SwapUsage_client2()
    #tree_client2_SwapUsage=parse_SwapUsage_client2()
    countlxml_SwapUsage_client2=count_client2_swap()
    countlxml_SwapSize_client2=count_client2_swap()
    TestDate_swap_client2 = root_node_client2_date_swap.findall("generic/SwapSize/TestDate")
    SwapUsage_client2 = root_node_client2_SwapUsage.findall("generic/SwapSize/SwapUsage")

    for Date_swap_client2 in TestDate_swap_client2:
        tab_client2_date_swap.append(Date_swap_client2.text)
        print('tab_client2_date', Date_swap_client2)

    for swapusage_client2 in SwapUsage_client2:
        tab_client2_SwapUsage.append(swapusage_client2.text)
        print('tab_client2_SwapUsage', tab_client2_SwapUsage)
    #tableau contenant les valeurs qu'on souhaite afficher
    #creer autant de ligne qu'il y a de balise <countlxml_SwapUsage_client2>
    d=0
    lst_swap_client2=[]

    for d in range(countlxml_SwapUsage_client2):
        lst_swap_client2.append(['SWAPusage',tab_client2_date_swap[d],tab_client2_SwapUsage[d],'Client2'])
        print('lst_swap_client2', lst_swap_client2)
    return lst_swap_client2
    return d
    return tab_client2_date
    return tab_client2_SwapUsage
declare -a github
declare -a path
NLINEA=1
conta=0
sorgente=0
configurazione=0
totale=0

function salva_file_in_array
{
    while  read  -r line
    do
        #echo "$line"
        github["$conta"]="$line"
        ((conta=conta+1))
    done  <  id_url_commit.txt
}


function clone_repo_diff
{
    mkdir -p collection
    cd collection
    for ((i=0; i<$conta; i+=2))
    do
        name1="repository"
        name2="$i"
        final_name="$name1$name2"
        mkdir -p "$final_name"
        cd "$final_name"
        git clone "${github["$i"]}"

        ls --group-directories-first> percorso.txt

        #legge solo la prima riga del file
        LINE=`head -n $NLINEA percorso.txt | tail -1`

        rm percorso.txt

        cd $LINE
        ((j=1+i))
        id_commit < ${github[$j]}
        #git show $id_commit
        git show $id_commit > C:/Users/ricca/Desktop/collection/"$final_name"/result.txt
        grep -i -n diff C:/Users/ricca/Desktop/collection/"$final_name"/result.txt > C:/Users/ricca/Desktop/collection/"$final_name"/result1.txt
        if [ -s C:/Users/ricca/Desktop/collection/"$final_name"/result.txt ]
        then
            echo pieno
            while IFS= read -r line; 
            do 
                touch C:/Users/ricca/Desktop/collection/line.txt
                echo $line > C:/Users/ricca/Desktop/collection/line.txt
                    
                ((totale+=1))
                echo "totale:"
                echo $totale
                if  grep   -n  '.js$\|.php$\|.cpp$\|.h$\|.jar$\|.c$\|.yml$\|.py$\|.java$\|.html$' <C:/Users/ricca/Desktop/collection/line.txt
                then
                    ((sorgente+=1))
                    echo "sorgente"
                    echo $sorgente
                    echo exist
                else
                    echo not exist
                    ((configurazione+=1))
                    echo "configurazione"
                    echo $configurazione
                fi
            done < C:/Users/ricca/Desktop/collection/"$final_name"/result1.txt
            rm C:/Users/ricca/Desktop/collection/line.txt

        else
            echo vuoto
            rm C:/Users/ricca/Desktop/collection/"$final_name"/result.txt
            rm C:/Users/ricca/Desktop/collection/"$final_name"/result1.txt
        
        fi
        
        cd C:/Users/ricca/Desktop/collection
        echo 
        echo finito $final_name
        echo
        
    done
            
    echo "totale:"
    echo $totale

separatore="/"
st="sorgente/totale:"
ct="configurazione/totale:"
s="$sorgente$separatore$totale"
c="$configurazione$separatore$totale"

sp=$((sorgente*100/totale))
cp=$((configurazione*100/totale))
cpp="$cp%"
spp="$sp%"

cd C:/Users/ricca/Desktop/collection
echo $st>conclusione.txt
echo $s>>conclusione.txt
echo $spp>>conclusione.txt
echo $ct>>conclusione.txt
echo $c>>conclusione.txt
echo $cpp>>conclusione.txt
}

function main
{
    salva_file_in_array
    clone_repo_diff
}

main


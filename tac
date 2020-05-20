program spelev3;
uses crt;

Const
Path = 'C:\logs.txt';

Var
File1:TextFile;

var p1x: array [1..5] of integer;
var p1y: array [1..5] of integer;

var p2x: array [1..5] of integer;
var p2y: array [1..5] of integer;

var z:string;
var sp1,sp2,i,x,y,r:integer;
var p1x1,p1x2,p1x3,p1y1,p1y2,p1y3,dio,dio2:integer;
var p2x1,p2x2,p2x3,p2y1,p2y2,p2y3,p2dio,p2dio2:integer;

procedure sakums();
	begin
	writeln('        .____,   |            |    ____   ."             _');
	writeln('       . \  / ,  |            |  ,` __ `.;           _  (_)');
	writeln('       |`-  -`|  |            | / ,`  ..`\         _| |_ _  ____ ');
	writeln('       |,-  -.|  |            | | | ;" | |        (_   _) |/ ___)');
	writeln('       ` /__\ `  |            | \ ;`__,` /          | |_| ( (___');
	writeln('        `    `   |            |  :.____,`            \__)_|\____)');
	writeln('    _____________|____________|_._____________');
	writeln('        .____,   |    ____    :`                         _');
	writeln('       . \  / ,  |  ,` __ ..."|                        _| |_ _____  ____');
	writeln('       |`-  -`|  | / ,` :". \ |                       (_   _|____ |/ ___)');
	writeln('       |,-  -.|  | | |..) | | |                         | |_/ ___ ( (___');
	writeln('       ` /__\ `  | \ ;.__,` / |                          \__)_____|\____)');
	writeln('        `    `   | .".____,`  |');
	writeln('    _____________:`___________|_______________               _   ');
	writeln('         ____  ""|            |   .____,                   _| |_ ___  _____');
	writeln('       ,` __ `:  |            |  . \  / ,                 (_   _) _ \| ___ |');
	writeln('      / ,`  ." \ |            |  |`-  -`|                   | || |_| | ____|');
	writeln('      | | .; | | |            |  |,-  -.|                    \__)___/|_____)');
	writeln('      \ .:__,` / |            |  ` /__\ `             ');
	writeln('       :.____,`  |            |   `    `             ');
	writeln('     :"');
	writeln();
	end;

procedure limenis();
begin
  writeln('Izvelies speles veidu.');
  writeln('[A].Speletajs1 pret Speletaju2.');
  writeln('[B].Speletajs1 pret Datoru.');
  readln(z);
end;

procedure laukums();
begin
  writeln();
  writeln('  Y') ;
  writeln(' ----------------');
  writeln('  1 |   |   |   |');
  writeln(' ----------------');
  writeln('  2 |   |   |   |');
  writeln(' ----------------');
  writeln('  3 |   |   |   |');
  writeln(' ----------------');
  writeln('    | 1 | 2 | 3 | X');
end;

procedure definicija();
begin
  for i:=1 to 5 do
  begin
  p1x[i]:=0;
  p1y[i]:=0;
  p2x[i]:=0;
  p2y[i]:=0;
  end;

  p1x1:=0;
  p1x2:=0;
  p1x3:=0;
  p1y1:=0;
  p1y2:=0;
  p1y3:=0;
  dio:=0;
  dio2:=0;

  p2x1:=0;
  p2x2:=0;
  p2x3:=0;
  p2y1:=0;
  p2y2:=0;
  p2y3:=0;
  p2dio:=0;
  p2dio2:=0;
end;

procedure izvade();

begin
  for i:=1 to 5 do
  begin
  GotoXY(3+4*p1x[i],2+2*p1y[i]);
  Write('X');
  end;

  for i:=1 to 5 do
  begin
  GotoXY(3+4*p2x[i],2+2*p2y[i]);
  Write('O');
  end;

  end;

procedure dzest();
begin
     GotoXY(1,12);
     for i:=1 to 10 do
     DelLine;
end;

procedure ievade();
begin

  repeat
  writeln('Ievadi x no 1 lidz 3:');
  readln(x);
  until (x>0) AND (x<4);

  repeat
  writeln('Ievadi y no 1 lidz 3:');
  readln(y);
  until (y>0) AND (y<4);

end;

procedure saglabasanaSp1(r:integer);
begin
  p1x[r]:=x;
  p1y[r]:=y;
end;

procedure saglabasanaSp2(r:integer);
begin
  p2x[r]:=x;
  p2y[r]:=y;
end;

procedure skaitsSp1(i:integer);
  begin
  if p1x[i] = 1 then
    p1x1:= p1x1+1
  else if p1x[i] = 2 then
    p1x2:= p1x2+1
  else if p1x[i] = 3 then
    p1x3:= p1x3+1;

    if p1y[i] = 1 then
    p1y1:= p1y1+1
  else if p1y[i] = 2 then
    p1y2:= p1y2+1
  else if p1y[i] = 3 then
    p1y3:= p1y3+1;

  if p1x[i]=p1y[i] then
    begin
      dio:=dio+1;
    end;

  if (p1x[i]=1) AND (p1y[i]=3) OR (p1x[i]=3) AND (p1y[i]=1)  then
    begin
      dio2:=dio2+1;
    end;

  if (p1x[i]=2) AND (p1y[i]=2) then
    begin
      dio2:=dio2+1;
    end;
 end;

procedure skaitsSp2(i:integer);
  begin
  if p2x[i] = 1 then
    p2x1:= p2x1+1
  else if p2x[i] = 2 then
    p2x2:= p2x2+1
  else if p2x[i] = 3 then
    p2x3:= p2x3+1;

    if p2y[i] = 1 then
    p2y1:= p2y1+1
  else if p2y[i] = 2 then
    p2y2:= p2y2+1
  else if p2y[i] = 3 then
    p2y3:= p2y3+1;

  if p2x[i]=p2y[i] then
    begin
      p2dio:=p2dio+1;
    end;

  if ((p2x[i]=1) AND (p2y[i]=3)) OR ((p2x[i]=3) AND (p2y[i]=1))  then
    begin
      p2dio2:=p2dio2+1;
    end;

  if (p2x[i]=2) AND (p2y[i]=2) then
    begin
      p2dio2:=p2dio2+1;
    end;
 end;

procedure p1win();
begin
  ClrScr;
  writeln('p1 ir uzvarejis');
  readln;
end;

procedure p2win();
begin
  ClrScr;
  writeln('p2 ir uzvarejis');
  readln;
end;

procedure neizskirts();
begin
  ClrScr;
  writeln('neizskirts');
  readln;
end;

procedure randoms();
begin
  randomize();
  begin
  x:= random(2) + 1;
  y:= random(2) + 1;
  end;

end;

function sp1skaits(n:integer): integer;
begin
   sp1:=n+1;
   sp1skaits:=sp1;
end;

function sp2skaits(n:integer): integer;
begin
   sp2:=n+1;
   sp2skaits:=sp2;
end;

begin
     sakums;
     writeln('Spied <Enter> lai saktu speli.');
     readln();
     ClrScr;
     definicija;
     sakums;
     limenis;

             repeat
             Case z of
             'A','B' :
             begin
             ClrScr;
             definicija;
             r:=0;
             laukums;
             GotoXY(30,5);
             writeln(sp1,': 1.Speletaja punkti');
             GotoXY(30,6);
             writeln(sp2,': 2.Speletaja punkti');
             repeat
             begin
             r:=r+1;
             dzest;
             ievade;

                 if ((p1x[1]=x) AND (p1y[1]=y)) OR ((p1x[2]=x) AND (p1y[2]=y)) OR ((p1x[3]=x) AND (p1y[3]=y)) OR ((p1x[4]=x) AND (p1y[4]=y)) OR ((p1x[5]=x) AND (p1y[5]=y)) OR
                  ((p2x[1]=x) AND (p2y[1]=y)) OR ((p2x[2]=x) AND (p2y[2]=y)) OR ((p2x[3]=x) AND (p2y[3]=y)) OR ((p2x[4]=x) AND (p2y[4]=y)) OR ((p2x[5]=x) AND (p2y[5]=y)) then
                  ievade;

             saglabasanaSp1(r);
             skaitsSp1(r);

             AssignFile(File1,Path);
             Rewrite(File1);
             Writeln(File1,'speletajs1 x: ',p1x[1],p1x[2],p1x[3],p1x[4],p1x[5]);
             Writeln(File1,'speletajs1 y: ',p1y[1],p1y[2],p1y[3],p1y[4],p1y[5]);
             Writeln(File1,'speletajs2 x: ',p1x[1],p1x[2],p1x[3],p1x[4],p1x[5]);
             Writeln(File1,'speletajs2 y: ',p2y[1],p2y[2],p2y[3],p2y[4],p2y[5]);
             Writeln(File1,'Gala rezultats: ',sp1,sp2);
             CloseFile(File1);

                 if (p1x1=3) OR (p1x2=3) OR (p1x3=3) OR (p1y1=3) OR (p1y2=3) OR (p1y3=3) OR (dio=3) OR (dio2=3) then
                   begin
                   p1win;
                   sp1skaits(sp1);
                   break;
                   end;

                 if r=5 then
                   begin
                   neizskirts;
                   break;
                   end;

             izvade;
             dzest;
             Case z of
             'A':
             begin
             ievade;

             if ((p1x[1]=x) AND (p1y[1]=y)) OR ((p1x[2]=x) AND (p1y[2]=y)) OR ((p1x[3]=x) AND (p1y[3]=y)) OR ((p1x[4]=x) AND (p1y[4]=y)) OR ((p1x[5]=x) AND (p1y[5]=y)) OR
                 ((p2x[1]=x) AND (p2y[1]=y)) OR ((p2x[2]=x) AND (p2y[2]=y)) OR ((p2x[3]=x) AND (p2y[3]=y)) OR ((p2x[4]=x) AND (p2y[4]=y)) OR ((p2x[5]=x) AND (p2y[5]=y)) then
                  ievade;

             saglabasanaSp2(r);
             skaitsSp2(r);
             izvade;

             if (p2x1=3) OR (p2x2=3) OR (p2x3=3) OR (p2y1=3) OR (p2y2=3) OR (p2y3=3) OR (p2dio=3) OR (p2dio2=3) then
                 begin
                 p2win;
                 sp2skaits(sp2);
                 break;
                 end
             end;

             'B':
             begin
             randoms;

             if ((p1x[1]=x) AND (p1y[1]=y)) OR ((p1x[2]=x) AND (p1y[2]=y)) OR ((p1x[3]=x) AND (p1y[3]=y)) OR ((p1x[4]=x) AND (p1y[4]=y)) OR ((p1x[5]=x) AND (p1y[5]=y)) OR
                 ((p2x[1]=x) AND (p2y[1]=y)) OR ((p2x[2]=x) AND (p2y[2]=y)) OR ((p2x[3]=x) AND (p2y[3]=y)) OR ((p2x[4]=x) AND (p2y[4]=y)) OR ((p2x[5]=x) AND (p2y[5]=y)) then
                 randoms;
             saglabasanaSp2(r);
             skaitsSp2(r);
             izvade;

             if (p2x1=3) OR (p2x2=3) OR (p2x3=3) OR (p2y1=3) OR (p2y2=3) OR (p2y3=3) OR (p2dio=3) OR (p2dio2=3) then
                 begin
                 p2win;
                 sp2skaits(sp2);
                 break;
                 end
             end;
             end;
             end
             until r=10;
        end;


        else
        Writeln('Ievadi A vai B!');
        readln(z);
        end;

        until r=10;

end.

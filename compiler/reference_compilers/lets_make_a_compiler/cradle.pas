{ This is a compiler based on http://compilers.iecc.com/crenshaw/
 NOTE: This particular compiler uses x86_64 for code generation rather than 
 dos 68000 }
{--------------------------------------------------------------}
program Cradle;

{--------------------------------------------------------------}
{ Constant Declarations }

const TAB = ^I;

{--------------------------------------------------------------}
{ Variable Declarations }

var Look: char;              { Lookahead Character }

{--------------------------------------------------------------}
{ Read New Character From Input Stream }

procedure GetChar;
begin
    Read(Look); { One character at a time }
end;

{--------------------------------------------------------------}
{ Report an Error }

procedure Error(s: string);
begin
    WriteLn; { assuming this means write a single new line? }
    WriteLn(^G, 'Error: ', s, '.'); { Not sure what ^G is. }
end;


{--------------------------------------------------------------}
{ Report Error and Halt }

procedure Abort(s: string);
begin
    Error(s);
    Halt; { No exit code? }
end;


{--------------------------------------------------------------}
{ Report What Was Expected }

procedure Expected(s: string);
begin
    Abort(s + ' Expected');
end;

{--------------------------------------------------------------}
{ Match a Specific Input Character }

procedure Match(x: char);
begin
    if Look = x then GetChar
    else Expected('''' + x + '''');
end;


{--------------------------------------------------------------}
{ Recognize an Alpha Character }

function IsAlpha(c: char): boolean;
begin
    IsAlpha := upcase(c) in ['A'..'Z'];
end;
                              

{--------------------------------------------------------------}

{ Recognize a Decimal Digit }

function IsDigit(c: char): boolean;
begin
    IsDigit := c in ['0'..'9'];
end;


{--------------------------------------------------------------}
{ Get an Identifier }

function GetName: char;
begin
    if not IsAlpha(Look) then Expected('Name');
    GetName := UpCase(Look);
    GetChar;
end;


{--------------------------------------------------------------}
{ Get a Number }

function GetNum: char;
begin
    if not IsDigit(Look) then Expected('Integer');
    GetNum := Look;
    GetChar;
end;


{--------------------------------------------------------------}
{ Output a String with Tab }

procedure Emit(s: string);
begin
    Write(TAB, s);
end;


{--------------------------------------------------------------}
{ Output a String with Tab and CRLF }

procedure EmitLn(s: string);
begin
    Emit(s);
    WriteLn;
end;

{--------------------------------------------------------------}
{ Initialize }

procedure Init;
begin
    { Grab the next character. Not doing token lookahead yet.}
    GetChar;
    { pre progoram boiler plate }
    EmitLn('.text');
    EmitLn('.globl _main');
    EmitLn('    _main:');
    EmitLn('    subq $8, %rsp');
end;

procedure Post;
begin
    { Post Program teardown. Always report program success for now. }
    EmitLn('    movq $0, %rdi');
    EmitLn('    call _exit');
end;

{---------------------------------------------------------------}
{ Parse and Translate an Expression }
procedure Term;
begin
    EmitLn('    movq $' + GetNum + ', %rax')
end;
{---------------------------------------------------------------}


{--------------------------------------------------------------}
{ Recognize and Translate an Add }

procedure Add;
begin
    Match('+');
    Term;
    EmitLn('    pop %rbx');
    EmitLn('    add %rax, %rbx');
end;


{-------------------------------------------------------------}
{ Recognize and Translate a Subtract }

procedure Subtract;
begin
    Match('-');
    Term;
    { TODO: Test if this subtractions rbx from rax or rax from rbx }
    { NOTE: potentially need to swithc the sign depending. }
    EmitLn('    pop %rbx');
    EmitLn('    sub %rax, %rbx');
end;
{-------------------------------------------------------------}


{---------------------------------------------------------------}
{ Parse and Translate an Expression }

procedure Expression;
begin
    Term;
    while Look in ['+', '-'] do begin
        EmitLn('    push %rax');
        case Look of
        '+': Add;
        '-': Subtract;
        else Expected('Addop');
        end;
    end;
end;
{--------------------------------------------------------------}

{--------------------------------------------------------------}
{ Main Program }

begin
    Init;
    Expression;
    Post;
end.
{--------------------------------------------------------------}

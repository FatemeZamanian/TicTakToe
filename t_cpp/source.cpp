#include <iostream>
#include <array>

using namespace std;


void show(char game[3][3]){
    cout<<endl;
    for(int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
        cout<<game[i][j];
    }
    cout<<endl;
    }
}

char check(char game[3][3]){
    char p='-';
    for(int i=0;i<3;i++){
        if (game[i][0]==game[i][1] && game[i][1]==game[i][2] && game[i][0] != '-'){
            p=game[i][0];
        }
        if (game[0][i]==game[1][i] && game[1][i]==game[2][i] && game[0][i] != '-'){
            p=game[0][i];

        }
    }

    if ((game[0][0]==game[1][1] && game[1][1]==game[2][2] && game[0][0] != '-') || (game[0][2]==game[1][1] && game[1][1]==game[2][0] && game[0][0] != '-')){
        p=game[0][0];
    }
    int c=0;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(game[i][j] != '-'){
                c++;

            }

        }
    }

    if (c==9 and p=='-'){
        p='n';
    }

    return p;
}


void play(int player,char game[3][3]){
    int row,col;
    while(1){
    if (player ==1){
        cout<<"player 1"<<endl;
    }
    else{
        cout<<"player 2"<<endl;
    }
    cout << "Enter row: ";
    cin>>row;
    cout << "Enter col: ";
    cin>>col;
    if (row<=2 && row>=0 && col<=2 && col>=0){
        if (game[row][col] == '-'){
            if (player ==1){
                game[row][col]='X';
                break;
            }

            else if (player ==2){
                game[row][col]='O';
                break;
            }
            
        }
        else{
            cout<<"Full place";
        }
    }
    else{
        cout<<"Wrong index";
    }
    }
}

void winner(char p){
    if(p=='n'){
        cout<<"No body wins"<<endl;
    }
    else if(p=='X'){
        cout<<"Player 1 wins"<<endl;
    }
    else if(p=='O'){
        cout<<"Player 1 wins"<<endl;
    }
}

int main(){
    char game[3][3];
    char p;
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            game[i][j]='-';
            cout<<game[i][j];
        }
    cout<<endl;
    }

    while(1){
    play(1,game);
    show(game);
    p=check(game);
    if(p != '-'){
        winner(p);
        return 0;
    }
    play(2,game);
    show(game);
    p=check(game);
    if(p != '-'){
        winner(p);
        return 0;
    }
    }
    return 0;

}


// g++ source.cpp
// ./a.out

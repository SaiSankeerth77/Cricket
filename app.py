from flask import Flask, render_template, request
import mysql.connector 

app = Flask(__name__)


def fetch_data(Team_ID="", Team_det="", Player_det="", Player_del=""):
    
    cnx = mysql.connector.connect(user='root', password='123456789',
                              host='localhost', database='cricket')

# Create a cursor object to execute queries
    cursor = cnx.cursor()
    
    if len(Team_ID)>=1:
        query = """
    SELECT * FROM Players WHERE team_id = {Id};
        """

        main_query = query.format(Id=Team_ID)
        cursor.execute(main_query)
        rows = cursor.fetchall()
        sequence = cursor.column_names
        main_data = []
        for result in rows:
            main_data.append(result)
        return(sequence, tuple(main_data))
        
    # get all the employee salaries greater than given input
    if len(Team_det)>=1:
        query = """

        SELECT
        T.name AS team_name,
        T.country,
        P.name AS player_name,
        P.role,
        P.batting_style,
        P.bowling_style
        FROM
        Cricket.Teams AS T
        JOIN
        Cricket.Players AS P ON T.team_id = P.team_id
        where T.team_id = {Id};
        
        """
        main_query = query.format(Id=Team_det)
        cursor.execute(main_query)
        rows = cursor.fetchall()
        sequence = cursor.column_names
        main_data = []
        for result in rows:
            main_data.append(result)
        return(sequence, tuple(main_data))
    
    if len(Player_det)>1:
        team_id, name, role, batting_style, bowling_style = Player_det.split(",")
        query = """
        INSERT INTO Players (team_id, name, role, batting_style, bowling_style) VALUES
        ({team_id},{name},"{role}","{batting_style}", "{bowling_style}");
        """
        main_query = query.format(team_id=team_id, name = name, role = role, batting_style = batting_style, bowling_style = bowling_style)
        cursor.execute(main_query)
        cnx.commit()

        query = """
        select * from Players;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        sequence = cursor.column_names
        main_data = []
        print(main_data)
        for result in rows:
            main_data.append(result)
        print(main_data)
        return(sequence, tuple(main_data))
    
    if len(Player_del)>=1:
         
        query = """

        Delete from Players
        where Players.name = "{Id}";
        
        """

        main_query = query.format(Id=Player_del)
        cursor.execute(main_query)
        cnx.commit()

        query = """
        select * from Players;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        sequence = cursor.column_names
        main_data = []
        print(main_data)
        for result in rows:
            main_data.append(result)
        print(main_data)
        return(sequence, tuple(main_data))
    
@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        Team_ID = request.form['Team_ID']
        Team_det = request.form['Team_det']
        Player_det = request.form['Player_det']
        Player_del = request.form['Player_del']
        headings, data = fetch_data(Team_ID, Team_det, Player_det, Player_del)
        return render_template("Main_page.html", headings=headings, data=data)
    return render_template("Main_page.html")


if __name__=="__main__":
    app.run(debug=True)
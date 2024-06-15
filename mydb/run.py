import argparse
import database

def add_team(args):
    database.add_team(args.name, args.city)
    print(f"Team '{args.name}' from '{args.city}' added successfully.")

def list_teams(args):
    teams = database.get_teams()
    for team in teams:
        print(f"ID: {team[0]}, Name: {team[1]}, City: {team[2]}")

def add_player(args):
    database.add_player(args.name, args.team_id, args.position)
    print(f"Player '{args.name}' added successfully.")

def list_players(args):
    players = database.get_players()
    for player in players:
        print(f"ID: {player[0]}, Name: {player[1]}, Team ID: {player[2]}, Position: {player[3]}")

def add_match(args):
    database.add_match(args.team1_id, args.team2_id, args.date, args.score)
    print(f"Match added successfully.")

def list_matches(args):
    matches = database.get_matches()
    for match in matches:
        print(f"ID: {match[0]}, Team1 ID: {match[1]}, Team2 ID: {match[2]}, Date: {match[3]}, Score: {match[4]}")

def get_team_id_by_name(name):
    teams = database.get_teams()
    for team in teams:
        if team[1] == name:
            return team[0]
    raise ValueError(f"Team '{name}' not found.")

def get_player_id_by_name(name):
    players = database.get_players()
    for player in players:
        if player[1] == name:
            return player[0]
    raise ValueError(f"Player '{name}' not found.")

def add_transfer(args):
    try:
        player_id = get_player_id_by_name(args.player_name)
        from_team_id = get_team_id_by_name(args.from_team_name)
        to_team_id = get_team_id_by_name(args.to_team_name)
        date = args.date
        fee = float(args.fee)
        
        database.add_transfer(player_id, from_team_id, to_team_id, date, fee)
        print("Transfer added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def list_transfers(args):
    transfers = database.get_transfers()
    for transfer in transfers:
        print(f"ID: {transfer[0]}, Player ID: {transfer[1]}, From Team ID: {transfer[2]}, To Team ID: {transfer[3]}, Date: {transfer[4]}, Fee: {transfer[5]}")

def add_loan(args):
    database.add_loan(args.player_id, args.from_team_id, args.to_team_id, args.start_date, args.end_date)
    print(f"Loan added successfully.")

def list_loans(args):
    loans = database.get_loans()
    for loan in loans:
        print(f"ID: {loan[0]}, Player ID: {loan[1]}, From Team ID: {loan[2]}, To Team ID: {loan[3]}, Start Date: {loan[4]}, End Date: {loan[5]}")

def main_menu():
    parser = argparse.ArgumentParser(description="Sports Management System CLI")
    subparsers = parser.add_subparsers()

    parser_add_team = subparsers.add_parser('add_team', help='Add a new team')
    parser_add_team.add_argument('name', type=str, help='Name of the team')
    parser_add_team.add_argument('city', type=str, help='City of the team')
    parser_add_team.set_defaults(func=add_team)

    parser_list_teams = subparsers.add_parser('list_teams', help='List all teams')
    parser_list_teams.set_defaults(func=list_teams)

    parser_add_player = subparsers.add_parser('add_player', help='Add a new player')
    parser_add_player.add_argument('name', type=str, help='Name of the player')
    parser_add_player.add_argument('team_id', type=int, help='ID of the team')
    parser_add_player.add_argument('position', type=str, help='Position of the player')
    parser_add_player.set_defaults(func=add_player)

    parser_list_players = subparsers.add_parser('list_players', help='List all players')
    parser_list_players.set_defaults(func=list_players)

    parser_add_match = subparsers.add_parser('add_match', help='Add a new match')
    parser_add_match.add_argument('team1_id', type=int, help='ID of the first team')
    parser_add_match.add_argument('team2_id', type=int, help='ID of the second team')
    parser_add_match.add_argument('date', type=str, help='Date of the match')
    parser_add_match.add_argument('score', type=str, help='Score of the match')
    parser_add_match.set_defaults(func=add_match)

    parser_list_matches = subparsers.add_parser('list_matches', help='List all matches')
    parser_list_matches.set_defaults(func=list_matches)

    parser_add_transfer = subparsers.add_parser('add_transfer', help='Add a new transfer')
    parser_add_transfer.add_argument('player_name', type=str, help='Name of the player')
    parser_add_transfer.add_argument('from_team_name', type=str, help='Name of the current team')
    parser_add_transfer.add_argument('to_team_name', type=str, help='Name of the new team')
    parser_add_transfer.add_argument('date', type=str, help='Date of the transfer')
    parser_add_transfer.add_argument('fee', type=float, help='Transfer fee')
    parser_add_transfer.set_defaults(func=add_transfer)

    parser_list_transfers = subparsers.add_parser('list_transfers', help='List all transfers')
    parser_list_transfers.set_defaults(func=list_transfers)

    parser_add_loan = subparsers.add_parser('add_loan', help='Add a new loan')
    parser_add_loan.add_argument('player_id', type=int, help='ID of the player')
    parser_add_loan.add_argument('from_team_id', type=int, help='ID of the current team')
    parser_add_loan.add_argument('to_team_id', type=int, help='ID of the new team')
    parser_add_loan.add_argument('start_date', type=str, help='Start date of the loan')
    parser_add_loan.add_argument('end_date', type=str, help='End date of the loan')
    parser_add_loan.set_defaults(func=add_loan)

    parser_list_loans = subparsers.add_parser('list_loans', help='List all loans')
    parser_list_loans.set_defaults(func=list_loans)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main_menu()

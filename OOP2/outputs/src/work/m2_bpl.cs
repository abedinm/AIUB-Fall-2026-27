using System;

class Player
{
    private string playerId;
    private string playerName;
    private string teamName;

    public string PlayerId
    {
        get { return playerId; }
        set { playerId = value; }
    }

    public string PlayerName
    {
        get { return playerName; }
        set { playerName = value; }
    }

    public string TeamName
    {
        get { return teamName; }
        set { teamName = value; }
    }

    public Player(string playerId,
        string playerName, string teamName)
    {
        this.playerId = playerId;
        this.playerName = playerName;
        this.teamName = teamName;
    }

    public virtual bool PlayerPerformance()
    {
        return false;
    }

    public virtual void ShowInfo()
    {
        Console.WriteLine("ID: " + playerId);
        Console.WriteLine("Name: " + playerName);
        Console.WriteLine("Team: " + teamName);
    }
}

class Batsman : Player
{
    private int totalRuns;
    private double battingAverage;
    private int highestScore;

    public Batsman(string playerId,
        string playerName, string teamName,
        int totalRuns, double battingAverage,
        int highestScore)
        : base(playerId, playerName, teamName)
    {
        this.totalRuns = totalRuns;
        this.battingAverage = battingAverage;
        this.highestScore = highestScore;
    }

    public override bool PlayerPerformance()
    {
        return battingAverage > 50;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();
        Console.WriteLine("Runs: " + totalRuns);
        Console.WriteLine("Average: " + battingAverage);
        Console.WriteLine("Highest: " + highestScore);
        if (PlayerPerformance())
        {
            Console.WriteLine("Eligible: Yes");
        }
        else
        {
            Console.WriteLine("Eligible: No");
        }
    }
}

class Bowler : Player
{
    private int totalWickets;
    private double bowlingAverage;

    public Bowler(string playerId,
        string playerName, string teamName,
        int totalWickets, double bowlingAverage)
        : base(playerId, playerName, teamName)
    {
        this.totalWickets = totalWickets;
        this.bowlingAverage = bowlingAverage;
    }

    public override bool PlayerPerformance()
    {
        return totalWickets > 100;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();
        Console.WriteLine("Wickets: " + totalWickets);
        Console.WriteLine("Average: " + bowlingAverage);
        if (PlayerPerformance())
        {
            Console.WriteLine("Eligible: Yes");
        }
        else
        {
            Console.WriteLine("Eligible: No");
        }
    }
}

class AllRounder : Player
{
    private int totalRuns;
    private int totalWickets;

    public AllRounder(string playerId,
        string playerName, string teamName,
        int totalRuns, int totalWickets)
        : base(playerId, playerName, teamName)
    {
        this.totalRuns = totalRuns;
        this.totalWickets = totalWickets;
    }

    public override bool PlayerPerformance()
    {
        return totalRuns > 1000 && totalWickets > 50;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();
        Console.WriteLine("Runs: " + totalRuns);
        Console.WriteLine("Wickets: " + totalWickets);
        if (PlayerPerformance())
        {
            Console.WriteLine("Eligible: Yes");
        }
        else
        {
            Console.WriteLine("Eligible: No");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Player[] players = new Player[4];
        players[0] = new Batsman("P-1", "Tom Latham",
            "NZ", 6789, 57.3, 183);
        players[1] = new Bowler("P-2", "Taskin Ahmed",
            "BD", 104, 23.2);
        players[2] = new AllRounder("P-3", "Glenn Maxwell",
            "AUS", 7598, 98);
        players[3] = new AllRounder("P-4", "Sam Curran",
            "Eng", 781, 60);

        foreach (Player player in players)
        {
            player.ShowInfo();
            Console.WriteLine();
        }
    }
}
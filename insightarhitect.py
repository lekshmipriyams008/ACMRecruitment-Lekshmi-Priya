import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filename):
    df = pd.read_csv(filename)
    return df

def create_histogram(df):
    plt.figure(figsize=(8, 5))

    plt.hist(df["math score"], bins=10, edgecolor="black")

    plt.title("Distribution of Math Scores")
    plt.xlabel("Math Score")
    plt.ylabel("Number of Students")

    plt.show()

def create_bar_chart(df):
    plt.figure(figsize=(8, 5))

    average_scores = df.groupby(
        "gender"
    )[["math score", "reading score", "writing score"]].mean()

    average_scores.plot(kind="bar")

    plt.title("Average Scores by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Score")

    plt.xticks(rotation=0)
    plt.legend(title="Subject")

    plt.tight_layout()
    plt.show()


def create_box_plot(df):
    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df[["math score", "reading score", "writing score"]]
    )

    plt.title("Distribution of Student Scores")
    plt.xlabel("Subject")
    plt.ylabel("Score")

    plt.show()


def create_scatter_plot(df):
    plt.figure(figsize=(8, 5))

    plt.scatter(
        df["math score"],
        df["reading score"],
        alpha=0.6
    )

    plt.title("Relationship Between Math and Reading Scores")
    plt.xlabel("Math Score")
    plt.ylabel("Reading Score")

    plt.grid(True)
    plt.show()

def create_heatmap(df):
    plt.figure(figsize=(7, 5))

    numerical_data = df[
        ["math score", "reading score", "writing score"]
    ]

    correlation = numerical_data.corr()

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Between Student Scores")

    plt.show()


def main():

    df = load_data("cleaned_students_performance.csv")

    print("Dataset loaded successfully!")
    print("Shape:", df.shape)

    create_histogram(df)
    create_bar_chart(df)
    create_box_plot(df)
    create_scatter_plot(df)
    create_heatmap(df)

if __name__ == "__main__":
    main()


from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

PROGRAMS = {
    "fat-loss": {
        "name": "Fat Loss (FL)",
        "workout": "Squats, cardio, bench press and recovery",
        "diet": "Egg whites, oats, grilled chicken and brown rice"
    },
    "muscle-gain": {
        "name": "Muscle Gain (MG)",
        "workout": "Squats, bench press, deadlifts and rows",
        "diet": "Eggs, oats, chicken and rice"
    },
    "beginner": {
        "name": "Beginner (BG)",
        "workout": "Air squats, ring rows and push-ups",
        "diet": "Balanced meals with adequate protein"
    }
}


@app.get("/")
def home():
    return render_template_string("""
    <h1>ACEest Fitness & Gym</h1>
    <p>Choose your fitness program:</p>
    <ul>
    {% for slug, program in programs.items() %}
      <li>
        <a href="/api/programs/{{ slug }}">
          {{ program.name }}
        </a>
      </li>
    {% endfor %}
    </ul>
    """, programs=PROGRAMS)


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/api/programs")
def get_programs():
    return jsonify(PROGRAMS)


@app.get("/api/programs/<slug>")
def get_program(slug):
    program = PROGRAMS.get(slug)

    if program is None:
        return jsonify({"error": "Program not found"}), 404

    return jsonify(program)


if __name__ == "__main__":
    app.run(debug=True)

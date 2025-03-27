from app import app, models
from app.models import Nombre, Comment
from sqlalchemy_data_model_visualizer import generate_data_model_diagram, add_web_font_and_interactivity

# List all your models
models = [Nombre, Comment]

# Set the output file name
output_file_name = 'my_data_model_diagram'

# Generate the diagram
generate_data_model_diagram(models, output_file_name)

# Add interactivity
add_web_font_and_interactivity('my_data_model_diagram.svg', 'my_interactive_data_model_diagram.svg')

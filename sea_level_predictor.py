import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
# This is way to generate a list of numbers
def generate_number_list(start, end, step):
  """
  Generates a list of numbers from start to end with a step size.

  Args:
      start: The starting number.
      end: The ending number (inclusive).
      step: The step size between numbers.

  Returns:
      A list of numbers from start to end with a step size of step.
  """

  number_list = list(range(start, end + step, step))
  list_length = len(number_list)  # Find the length of the list
  return number_list, list_length  # Return both the list and its length

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    year = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']
    plt.scatter(year, sea_level)


    # Create first line of best fit
    # Function to generate fitted line points
    def fitted_line(x):
        return slope * x + intercept
    
    slope, intercept, r_value, p_value, std_err = linregress(year, sea_level)

    # Generate x-values for smooth line (optional, adjust range as needed)
    x_vals, x_vals_length = generate_number_list(1880, 2050, 1)
    plt.plot(years_for_plot, [fitted_line(y) for y in years_for_plot], 'r-', label='Best Fit Line (all data)')

    # Create second line of best fit
    #New fitted line function
    def fitted_line_2000(x):
        return slope_2000 * x + intercept_2000

    # Filter data for after 2000
    year_2000_onwards = year[year >= 2000]
    sea_level_2000_onwards = sea_level[year >= 2000]

    # Perform linear regression for post-2000 data
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(year_2000_onwards, sea_level_2000_onwards)

    # the 2050 year
    years_for_plot2, years_for_plot2_len = generate_number_list(2000, 2050, 1)
    # Plot the second best fit line (2000 onwards)
    plt.plot(years_for_plot2, [fitted_line_2000(y) for y in years_for_plot2], 'm-', label='Best Fit Line (2000 onward)')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
# maxlength-maxtext
A component that displays chips with ability to specify maximum length and text in a chip
It accepts three parameters: chips: the array of chips, maxChips: the maximum number of chips displayed, and maxTextLength: the maximum length of text in a chip

# How It Works
The number of displayed chips will be controlled by the maxChips parameter.
If the maximum number of chips to be displayed is exceeded, the number of chips that are not shown in the aside element is indicated with data-testid="exceeding-text".
The length of text in each chip will be controlled by the maxTextLength parameter.
If the maximum length of text in a chip is exceeded, an ellipsis symbol (…) is attached after the last allowed letter
ChipList is the component that will be tested against a set of Unit Tests. The App component is only used for simulating the behavior in the Preview tab; it will be not used in the Unit Tests.
The chips are displayed in the same order as they appear in the chips property. Indexes are provided for each chip in the data-testid property.

# Techologies Used
We used python libraries in creating this component

# Contributors
Valerine Chemutai
Sadiq Said
Eunice Mwenda
Newton Bundi



from PIL import Image, ImageChops

def test_click_second_valve_type(valve_design_page):
    # Open dropdown and select second option
    valve_design_page.open_dropdown()
    option_text = valve_design_page.select_second_valve_type()

    # Assert option text is valid
    assert option_text, "Second option text should not be empty"
    print(f" Clicked on dropdown option: {option_text}")

    #Move slider using pixels on x axis and take screenshot
    valve_design_page.set_valve_diameter_slider(25)

    # valve_design_page.set_valve_diameter_slider(100)
    valve_design_page.take_screenshot("current.png")
    # Compare with baseline image
    assert compare_images("current.png", "baseline.png", "diff.png"), "Images do not match!"


#Helper Method
def compare_images(img_path1, img_path2, diff_path=None, tolerance=5):
    """Compare two images with a pixel tolerance."""
    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)
    diff = ImageChops.difference(img1, img2)
    if diff_path:
        diff.save(diff_path)
    # Count non-zero pixels in the diff image
    bbox = diff.getbbox()
    if not bbox:
        return True  # Images are exactly the same
    # Calculate total difference
    diff_pixels = sum(diff.crop(bbox).convert("L").point(lambda x: x > tolerance and 1).getdata())
    total_pixels = diff.crop(bbox).size[0] * diff.crop(bbox).size[1]
    # Allow up to 1% difference
    return diff_pixels / total_pixels < 0.01

    
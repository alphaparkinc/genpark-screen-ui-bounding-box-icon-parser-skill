from client import ScreenUiBoundingBoxIconParserClient

def main():
    client = ScreenUiBoundingBoxIconParserClient()
    res = client.parse_screen_interactive_elements(2560, 1440)
    print('OmniParser Screen UI: ' + res['screen_parse_id'] + ' (' + str(res['interactive_elements_detected_count']) + ' elements)')
    print('Icons: ' + str(res['clickable_icons_count']) + ' | Input Fields: ' + str(res['text_input_fields_count']))
    print('Bounding Box AST: ' + res['bounding_boxes_normalized_ast_url'])
    print('SoM Image: ' + res['annotated_som_screenshot_url'])

if __name__ == '__main__':
    main()

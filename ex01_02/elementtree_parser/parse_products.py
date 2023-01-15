from xml.etree.ElementTree import parse


def parse_xml_to_list(xml_file_path):
    document = parse(xml_file_path)
    products_node = document.getroot()

    product_list = []
    for product_node in products_node:
        product = {'id': product_node.attrib['product-id']}
        for child_node in product_node:
            product[child_node.tag] = child_node.text
        product_list.append(product)
    return product_list


if __name__ == '__main__':
    from pprint import pprint

    products = parse_xml_to_list('../data/products.xml')
    pprint(products)

from re import L


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children=children
        self.props=props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f'tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}'

    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.tag == "img":
            props_html = self.props_to_html()
            return f"<img{props_html}/>"
        if not self.value:
            raise ValueError
        if self.tag is None:
            return self.value
        else:
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag, value=None, children=children, props=None)

    def to_html(self):
        if not self.tag:
            raise ValueError('No Tag')
        
        children_html = ""
        if not self.children or len(self.children) == 0:
            raise ValueError('No Children')
        for child in self.children:
            children_html += child.to_html()
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"

    
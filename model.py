def Main(x, y):
    return f"""
local IMAGE = Instance.new("ScreenGui")
local Background = Instance.new("Frame")
local UIGridLayout = Instance.new("UIGridLayout")

IMAGE.Name = "IMAGE"
IMAGE.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui")
IMAGE.ZIndexBehavior = Enum.ZIndexBehavior.Sibling

Background.Name = "Background"
Background.Parent = IMAGE
Background.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
Background.BorderSizePixel = 0
Background.Size = UDim2.new(0, {x}, 0, {y})
Background.ClipsDescendants = true

UIGridLayout.Parent = Background
UIGridLayout.SortOrder = Enum.SortOrder.LayoutOrder
UIGridLayout.CellSize = UDim2.new(0, 1, 0, 1)
UIGridLayout.CellPadding = UDim2.new(0, 1, 0, 1)

function CreatePixel(x, y, z)
	local Pixel = Instance.new("Frame")

	Pixel.Name = "Pixel"
	Pixel.Parent = Background
	Pixel.BackgroundColor3 = Color3.fromRGB(x, y, z)
	Pixel.BorderSizePixel = 0
	Pixel.Size = UDim2.new(0, 90, 0, 95)
end\n\n
"""

def Pixel(x, y, z):
    return f"CreatePixel({x}, {y}, {z})\n"
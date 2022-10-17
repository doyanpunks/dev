#include <wrl/client.h>
#include <d3d11.h>
#include <exception>
#include <DirectXHelper.h>



int main()
{
	Microsoft::WRL::ComPtr<ID3D11RenderTargetView> m_renderTargetView;
	UINT creationFlags = D3D11_CREATE_DEVICE_BGRA_SUPPORT;

#if defined(_DEBUG)
	// If the project is in a debug build, enable debugging via SDK Layers with this flag.
	creationFlags |= D3D11_CREATE_DEVICE_DEBUG;
#endif

	D3D_FEATURE_LEVEL featureLevels[] =
	{
		D3D_FEATURE_LEVEL_11_1,
		D3D_FEATURE_LEVEL_11_0,
		D3D_FEATURE_LEVEL_10_1,
		D3D_FEATURE_LEVEL_10_0,
		D3D_FEATURE_LEVEL_9_3,
		D3D_FEATURE_LEVEL_9_1
	};

	Microsoft::WRL::ComPtr<ID3D11Device> d3dDevice;
	Microsoft::WRL::ComPtr<ID3D11DeviceContext> m_d3dDeviceContext;
	DX::ThrowIfFailed();

	m_d3dDeviceContext->OMSetRenderTargets(
		1,
		m_renderTargetView.GetAddressOf(),
		nullptr
	);
	return 0;
}
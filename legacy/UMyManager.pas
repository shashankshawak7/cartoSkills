unit UMyManager;

interface

uses
  System.SysUtils, System.Classes, UBaseManager;

type
  TMyManager = class(TBaseManager)
  private
    FOrderID: Integer;
    FTotal: Double;
    FOnProcessComplete: TNotifyEvent;
    procedure SetTotal(const Value: Double);
  protected
    procedure DoComplete; virtual;
  public
    constructor Create; override;
    destructor Destroy; override;
    procedure Process(ID: Integer); override;
    property OrderID: Integer read FOrderID write FOrderID;
    property Total: Double read FTotal write SetTotal;
    property OnProcessComplete: TNotifyEvent read FOnProcessComplete write FOnProcessComplete;
  end;

var
  GGlobalCounter: Integer = 0;

implementation

{ TMyManager }

constructor TMyManager.Create;
begin
  inherited Create;
  FOrderID := 0;
  FTotal := 0.0;
end;

destructor TMyManager.Destroy;
begin
  // Resource Cleanup
  inherited Destroy;
end;

procedure TMyManager.SetTotal(const Value: Double);
begin
  if FTotal <> Value then
  begin
    FTotal := Value;
    Inc(GGlobalCounter); // Side effect: Modifies unit global
  end;
end;

procedure TMyManager.DoComplete;
begin
  if Assigned(FOnProcessComplete) then
    FOnProcessComplete(Self);
end;

procedure TMyManager.Process(ID: Integer);
begin
  OrderID := ID;
  try
    // Simulation of complex logic
    inherited Process(ID);
    Total := Total + 100.50;
    DoComplete;
  finally
    // Ensure memory/state safety
    LogProcess(ID);
  end;
end;

end.
